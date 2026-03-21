from flask import Blueprint, render_template

from bussdcc_framework.web import current_ctx

bp = Blueprint("home", __name__)


@bp.route("/")
def index() -> str:
    config = current_ctx().state.get("config")
    return render_template("home/index.html", config=config)
