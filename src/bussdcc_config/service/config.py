from dataclasses import asdict

from bussdcc import Service, ContextProtocol, Event, Message

from .. import config
from .. import message


class ConfigService(Service):
    name = "config"

    def __init__(self, data_dir: str) -> None:
        self._data_dir = data_dir

    def _save_config(self, ctx: ContextProtocol) -> None:
        cfg = ctx.state.get("config")
        if cfg:
            self.cs.data = asdict(cfg)
            self.cs.save()
            ctx.emit(message.ConfigSaved())

    def start(self, ctx: ContextProtocol) -> None:
        self.cs = config.ConfigStore(f"{self._data_dir}/config.json")
        if self.cs.data:
            ctx.emit(message.ConfigInitialized(self.cs.data))

    def handle_event(self, ctx: ContextProtocol, evt: Event[Message]) -> None:
        if isinstance(evt.payload, message.ConfigChanged):
            self._save_config(ctx)

    def stop(self, ctx: ContextProtocol) -> None:
        self._save_config(ctx)
