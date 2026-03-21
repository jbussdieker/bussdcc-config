from dataclasses import dataclass

from bussdcc import Message

from .. import config


@dataclass(slots=True, frozen=True)
class ConfigInitialized(Message):
    config: config.Config


@dataclass(slots=True, frozen=True)
class ConfigUpdate(Message):
    config: config.Config


@dataclass(slots=True, frozen=True)
class ConfigChanged(Message):
    pass


@dataclass(slots=True, frozen=True)
class ConfigSaved(Message):
    pass
