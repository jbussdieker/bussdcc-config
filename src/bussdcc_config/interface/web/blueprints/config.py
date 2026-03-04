from typing import Any
from dataclasses import asdict
from flask import Blueprint, render_template, redirect, url_for, request

from bussdcc_framework.interface.web import current_ctx

from .... import message, config

bp = Blueprint("config", __name__, url_prefix="/config")


@bp.route("/", methods=["GET", "POST"])
def index() -> Any:
    ctx = current_ctx()

    if request.method == "GET":
        cfg = ctx.state.get("config")
        schema = config.build_schema(cfg)
        groups = config.group_schema(schema)
        return render_template("config/index.html", groups=groups)

    elif request.method == "POST":
        cfg = config.Config.from_dict(request.form)
        ctx.emit(message.ConfigUpdate(data=asdict(cfg)))
        return redirect(url_for("home.index"))
