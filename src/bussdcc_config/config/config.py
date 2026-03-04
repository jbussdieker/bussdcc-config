from dataclasses import dataclass, asdict, field

from typing import Any, List, Literal


@dataclass(slots=True, frozen=True)
class Config:
    name: str = field(metadata={"label": "Name"})
    active: bool = field(metadata={"label": "Active"})
    age: int = field(
        metadata={
            "label": "Age",
            "group": "Details",
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

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Config":
        return Config(
            name=data.get("name", ""),
            age=int(data.get("age", 0)),
            sex=data.get("sex", "male"),
            active=bool(data.get("active")),
        )
