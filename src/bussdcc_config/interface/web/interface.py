from typing import Any

from flask import redirect, url_for, request
from flask_socketio import SocketIO

from bussdcc import ContextProtocol, Event, Message
from bussdcc_framework.web import FlaskApp, WebInterface as Base

from .blueprints.home import bp as home_bp
from .blueprints.config import bp as config_bp

from ... import message


class WebInterface(Base):
    def register_routes(self, app: FlaskApp, ctx: ContextProtocol) -> None:
        app.register_blueprint(home_bp)
        app.register_blueprint(config_bp)

        @app.before_request
        def initial_configuration() -> Any:
            cfg = ctx.state.get("config")
            if cfg is not None:
                return

            allowed_endpoints = {"config.new", "config.update", "static"}
            if request.endpoint not in allowed_endpoints:
                return redirect(url_for("config.new"))

        @app.context_processor
        def get_context() -> dict[str, Any]:
            system_identity = ctx.state.get("system.identity")

            return dict(
                system_identity=system_identity,
            )

    def handle_event(self, ctx: ContextProtocol, evt: Event[Message]) -> None:
        if isinstance(evt.payload, message.ConfigChanged):
            cfg = ctx.state.get("config")
            self.socketio.emit("ui.config.changed", cfg)
