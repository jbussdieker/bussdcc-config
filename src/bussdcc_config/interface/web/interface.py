from typing import Any
from dataclasses import asdict

from flask import redirect, url_for, request
from flask_socketio import SocketIO

from bussdcc.process import Process
from bussdcc.context import ContextProtocol
from bussdcc.event import Event
from bussdcc.message import Message

from bussdcc_framework.interface.web import WebInterface as Base
from bussdcc_framework.interface.web.base import FlaskApp

from .blueprints.home import bp as home_bp
from .blueprints.config import bp as config_bp
from .blueprints.debug import bp as debug_bp

from ... import message


class WebInterface(Base):
    def register_routes(self, app: FlaskApp, ctx: ContextProtocol) -> None:
        app.register_blueprint(home_bp)
        app.register_blueprint(config_bp)
        app.register_blueprint(debug_bp)

        @app.before_request
        def initial_configuration() -> Any:
            cfg = ctx.state.get("config")
            if cfg is not None:
                return

            allowed_endpoints = {"config.new", "config.update", "debug.index", "static"}
            if request.endpoint not in allowed_endpoints:
                return redirect(url_for("config.new"))

        @app.context_processor
        def get_context() -> dict[str, Any]:
            system_identity = ctx.state.get("system.identity")

            return dict(
                system_identity=system_identity,
            )

    def register_socketio(self, socketio: SocketIO, ctx: ContextProtocol) -> None:
        pass
        # @socketio.on("ui.config.set")
        # def config_update(data: dict[str, str]) -> None:
        #    ctx.emit(message.ConfigSet(key=data["key"], value=data["value"]))

    def handle_event(self, ctx: ContextProtocol, evt: Event[Message]) -> None:
        if isinstance(evt.payload, message.ConfigChanged):
            cfg = ctx.state.get("config")
            self.socketio.emit("ui.config.changed", cfg)
