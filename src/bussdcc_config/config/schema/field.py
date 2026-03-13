from dataclasses import dataclass, Field
from typing import Any, Literal, get_origin, get_args, Type

from .field_meta import FieldMeta


@dataclass(slots=True, frozen=True)
class SchemaField:
    name: str
    type: Type[object] | str
    meta: FieldMeta
    value: Any | None = None
    ui: str | None = None
    options: list[str] | None = None

    @staticmethod
    def from_field(f: Field[object], value: Any | None = None) -> "SchemaField":
        meta = FieldMeta.from_field(f)

        origin = get_origin(f.type)
        args = get_args(f.type)

        ui = meta.ui
        options = None

        if origin is Literal:
            ui = "select"
            options = list(args)

        if not ui:
            if f.type in (int, float):
                ui = "number"
            elif f.type is bool:
                ui = "checkbox"
            else:
                ui = "text"

        return SchemaField(
            name=f.name,
            type=f.type,
            meta=meta,
            value=value,
            ui=ui,
            options=options,
        )
