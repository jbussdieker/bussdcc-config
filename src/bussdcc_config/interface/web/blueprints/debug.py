from flask import Blueprint, render_template

from bussdcc_framework.interface.web import current_ctx

bp = Blueprint("debug", __name__, url_prefix="/debug")


@bp.route("/")
def index() -> str:
    state_store = current_ctx().state
    if hasattr(state_store, "_state"):
        state = state_store._state
    else:
        state = {}

    config = current_ctx().state.get("config")

    return render_template("debug/index.html", state=state, config=config)
