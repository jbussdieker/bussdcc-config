from dataclasses import dataclass

from bussdcc import Message

from ..config import Config


@dataclass(slots=True, frozen=True)
class ConfigInitialized(Message):
    config: Config


@dataclass(slots=True, frozen=True)
class ConfigUpdate(Message):
    config: Config


@dataclass(slots=True, frozen=True)
class ConfigChanged(Message):
    pass


@dataclass(slots=True, frozen=True)
class ConfigSaved(Message):
    pass
