from dataclasses import dataclass, Field
from typing import Any, Literal, get_origin, get_args
from datetime import date, time, datetime
from enum import Enum

from .field_meta import FieldMeta


@dataclass(slots=True, frozen=True)
class SchemaField:
    name: str
    type: object
    meta: FieldMeta
    value: Any | None = None
    input_type: str | None = None
    options: list[str] | None = None

    @staticmethod
    def from_field(f: Field[object], value: Any | None = None) -> "SchemaField":
        meta = FieldMeta.from_field(f)

        tp = f.type
        origin = get_origin(tp)
        args = get_args(tp)

        input_type: str | None = None
        options: list[str] | None = None

        if origin is Literal:
            input_type = "select"
            options = [str(v) for v in args]

        elif isinstance(tp, type) and issubclass(tp, Enum):
            input_type = "select"
            options = [str(member.value) for member in tp]

            if isinstance(value, Enum):
                value = value.value

        elif tp in (int, float):
            input_type = "number"
        elif tp is bool:
            input_type = "checkbox"
        elif tp is date:
            input_type = "date"
        elif tp is time:
            input_type = "time"
        elif tp is datetime:
            input_type = "datetime-local"
        else:
            input_type = "text"

        return SchemaField(
            name=f.name,
            type=tp,
            meta=meta,
            value=value,
            input_type=input_type,
            options=options,
        )
