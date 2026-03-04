from typing import Any

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
        pass
        # if isinstance(evt.payload, message.SnapshotUpdated):
        #    payload = {
        #        "timestamp": evt.time.timestamp() * 1000 if evt.time else None,
        #        **ctx.state.get("snapshot"),
        #    }
        #    self.socketio.start_background_task(
        #        self.socketio.emit, "ui.snapshot.updated", payload
        #    )
