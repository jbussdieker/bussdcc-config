from dataclasses import dataclass, asdict, Field
from typing import Optional, Literal, Any, get_origin, get_args
from types import MappingProxyType


@dataclass(slots=True, frozen=True)
class FieldMeta:
    label: str
    group: str = "General"
    required: bool = False
    ui: str | None = None
    help: str | None = None
    min: int | float | None = None
    max: int | float | None = None
    step: int | float | None = None

    @staticmethod
    def from_field(f: Field[object]) -> "FieldMeta":
        meta: MappingProxyType[Any, Any] = f.metadata

        return FieldMeta(
            label=meta.get("label", f.name),
            group=meta.get("group", "General"),
            required=meta.get("required", False),
            ui=meta.get("ui"),
            help=meta.get("help"),
            min=meta.get("min"),
            max=meta.get("max"),
            step=meta.get("step"),
        )
