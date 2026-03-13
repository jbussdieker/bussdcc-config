from dataclasses import dataclass, asdict, field

from typing import Any, List, Literal


@dataclass(slots=True, frozen=True)
class Database:
    host: str = field(metadata={"label": "Host", "group": "Database"})
    port: int = field(metadata={"label": "Port", "group": "Database"})


@dataclass(slots=True, frozen=True)
class Config:
    name: str = field(metadata={"label": "Name", "required": True, "help": "Full name"})

    active: bool = field(
        metadata={"label": "Active", "help": "User account active status"}
    )

    age: int = field(
        metadata={
            "label": "Age",
            "group": "Details",
            "required": True,
            "ui": "number",
            "help": "Age on the date filling this out",
            "min": 0,
            "max": 120,
            "step": 1,
        },
    )

    sex: Literal["male", "female"] = field(
        metadata={"label": "Sex", "group": "Details"}
    )

    database: Database
