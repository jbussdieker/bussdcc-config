import json
from typing import Any
from dataclasses import asdict
from flask import Blueprint, render_template, redirect, url_for, request

from bussdcc_framework.interface.web import current_ctx
from bussdcc_framework.util import build_dataclass
from bussdcc_framework import json as framework_json

from .... import message, config

from ....config import schema

bp = Blueprint("config", __name__, url_prefix="/config")


@bp.route("/")
def index() -> Any:
    ctx = current_ctx()
    cfg = ctx.state.get("config")
    s = schema.build(cfg)
    fields = schema.flatten(s)
    groups = schema.group(fields)
    return render_template(
        "config/index.html", groups=groups, action=url_for("config.update")
    )


@bp.route("/update", methods=["POST"])
def update() -> Any:
    ctx = current_ctx()
    s = schema.build(config.Config)
    data = schema.unflatten(s, request.form)
    cfg = build_dataclass(config.Config, data)
    ctx.emit(message.ConfigUpdate(data=asdict(cfg)))
    return redirect(url_for("home.index"))


@bp.route("/new")
def new() -> Any:
    s = schema.build(config.Config)
    fields = schema.flatten(s)
    groups = schema.group(fields)
    return render_template(
        "config/new.html", groups=groups, action=url_for("config.update")
    )
