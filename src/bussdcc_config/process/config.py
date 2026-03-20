from bussdcc import Process, ContextProtocol, Event, Message

from .. import message, config


class ConfigProcess(Process):
    name = "config"

    def handle_event(self, ctx: ContextProtocol, evt: Event[Message]) -> None:
        if isinstance(evt.payload, message.ConfigInitialized):
            ctx.state.set("config", evt.payload.config)
        elif isinstance(evt.payload, message.ConfigUpdate):
            ctx.state.set("config", evt.payload.config)
            ctx.emit(message.ConfigChanged())
