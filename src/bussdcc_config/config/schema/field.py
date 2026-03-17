from dataclasses import dataclass, Field
from typing import Any, Literal, get_origin, get_args, Union
from datetime import date, time, datetime
from enum import Enum
import types

from .field_meta import FieldMeta


def _unwrap_optional(tp: object) -> object:
    origin = get_origin(tp)
    args = get_args(tp)

    if origin in (Union, types.UnionType):
        non_none = [arg for arg in args if arg is not type(None)]
        if len(non_none) == 1:
            return non_none[0]

    return tp


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
        base_tp = _unwrap_optional(tp)

        origin = get_origin(base_tp)
        args = get_args(base_tp)

        input_type: str | None = None
        options: list[str] | None = None

        if origin is Literal:
            input_type = "select"
            options = [str(v) for v in args]

        elif isinstance(base_tp, type) and issubclass(base_tp, Enum):
            input_type = "select"
            options = [str(member.value) for member in base_tp]

            if isinstance(value, Enum):
                value = value.value

        elif base_tp in (int, float):
            input_type = "number"
        elif base_tp is bool:
            input_type = "checkbox"
        elif base_tp is date:
            input_type = "date"
        elif base_tp is time:
            input_type = "time"
        elif base_tp is datetime:
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
