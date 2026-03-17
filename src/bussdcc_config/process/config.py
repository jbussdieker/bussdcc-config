from bussdcc import Process, ContextProtocol, Event, Message
from bussdcc_framework.util import build_dataclass

from .. import message, config


class ConfigProcess(Process):
    name = "config"

    def handle_event(self, ctx: ContextProtocol, evt: Event[Message]) -> None:
        if isinstance(evt.payload, message.ConfigInitialized):
            ctx.state.set("config", build_dataclass(config.Config, evt.payload.data))
        elif isinstance(evt.payload, message.ConfigUpdate):
            ctx.state.set("config", build_dataclass(config.Config, evt.payload.data))
            ctx.emit(message.ConfigChanged())
