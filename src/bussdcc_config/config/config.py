from dataclasses import dataclass, asdict, field

from typing import Any, List, Literal
from datetime import date, time, datetime


@dataclass(slots=True, frozen=True)
class Database:
    host: str = field(metadata={"label": "Host", "group": "Database"})
    port: int = field(metadata={"label": "Port", "group": "Database"})


@dataclass(slots=True, frozen=True)
class Setting:
    key: str = field(metadata={"label": "Key"})
    value: int = field(metadata={"label": "Value"})


@dataclass(slots=True, frozen=True)
class Config:
    name: str = field(metadata={"label": "Name", "required": True, "help": "Full name"})
    database: Database
    settings: list[Setting]
    params: dict[str, Setting]
