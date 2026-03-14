from dataclasses import dataclass, Field
from typing import Any, Literal, get_origin, get_args, Type
from datetime import date, time, datetime

from .field_meta import FieldMeta


@dataclass(slots=True, frozen=True)
class SchemaField:
    name: str
    type: Type[object] | str
    meta: FieldMeta
    value: Any | None = None
    input_type: str | None = None
    options: list[str] | None = None

    @staticmethod
    def from_field(f: Field[object], value: Any | None = None) -> "SchemaField":
        meta = FieldMeta.from_field(f)

        origin = get_origin(f.type)
        args = get_args(f.type)

        input_type = None
        options = None

        if origin is Literal:
            input_type = "select"
            options = list(args)

        if input_type is None:
            if f.type in (int, float):
                input_type = "number"
            elif f.type is bool:
                input_type = "checkbox"
            elif f.type is date:
                input_type = "date"
            elif f.type is time:
                input_type = "time"
            elif f.type is datetime:
                input_type = "datetime-local"
            else:
                input_type = "text"

        return SchemaField(
            name=f.name,
            type=f.type,
            meta=meta,
            value=value,
            input_type=input_type,
            options=options,
        )
