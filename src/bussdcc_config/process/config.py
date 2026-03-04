from bussdcc import Process, ContextProtocol, Event, Message

from .. import message, config


class ConfigProcess(Process):
    name = "config"

    def handle_event(self, ctx: ContextProtocol, evt: Event[Message]) -> None:
        if isinstance(evt.payload, message.ConfigInitialized):
            ctx.state.set("config", config.Config.from_dict(evt.payload.data))
        elif isinstance(evt.payload, message.ConfigUpdate):
            ctx.state.set("config", config.Config.from_dict(evt.payload.data))
            ctx.emit(message.ConfigChanged())
