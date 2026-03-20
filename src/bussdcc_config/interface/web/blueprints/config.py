from typing import Any
from flask import Blueprint, render_template, redirect, url_for, request

from bussdcc_framework.interface.web import current_ctx
from bussdcc_framework.codec import load_value

from .... import message, config

from ....config import formtree

bp = Blueprint("config", __name__, url_prefix="/config")


@bp.route("/")
def index() -> Any:
    ctx = current_ctx()
    cfg = ctx.state.get("config")
    tree = formtree.build(cfg)
    return render_template(
        "config/index.html", tree=tree, action=url_for("config.update")
    )


@bp.route("/update", methods=["POST"])
def update() -> Any:
    ctx = current_ctx()
    tree = formtree.build(config.Config)
    data = formtree.unflatten(tree, request.form)
    cfg = load_value(config.Config, data)
    ctx.emit(message.ConfigUpdate(config=cfg))
    return redirect(url_for("home.index"))


@bp.route("/new")
def new() -> Any:
    tree = formtree.build(config.Config)
    return render_template(
        "config/new.html", tree=tree, action=url_for("config.update")
    )
