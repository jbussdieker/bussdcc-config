from typing import Any
from dataclasses import asdict
from flask import Blueprint, render_template, redirect, url_for, request

from bussdcc_framework.interface.web import current_ctx

from .... import message, config

bp = Blueprint("config", __name__, url_prefix="/config")


@bp.route("/")
def index() -> Any:
    ctx = current_ctx()
    cfg = ctx.state.get("config")
    schema = config.schema(cfg)
    return render_template(
        "config/index.html", schema=schema, action=url_for("config.update")
    )


@bp.route("/update", methods=["POST"])
def update() -> Any:
    ctx = current_ctx()
    cfg = config.Config.from_dict(request.form)
    ctx.emit(message.ConfigUpdate(data=asdict(cfg)))
    return redirect(url_for("home.index"))


@bp.route("/new")
def new() -> Any:
    schema = config.schema(config.Config)
    return render_template(
        "config/new.html", schema=schema, action=url_for("config.update")
    )
