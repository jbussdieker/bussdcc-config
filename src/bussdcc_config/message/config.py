from dataclasses import dataclass

from bussdcc import Message


@dataclass(slots=True, frozen=True)
class ConfigInitialized(Message):
    data: dict[str, object]


@dataclass(slots=True, frozen=True)
class ConfigUpdate(Message):
    data: dict[str, object]


@dataclass(slots=True, frozen=True)
class ConfigChanged(Message):
    pass


@dataclass(slots=True, frozen=True)
class ConfigSaved(Message):
    pass
