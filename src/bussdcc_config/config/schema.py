from typing import Literal
from dataclasses import dataclass, fields, is_dataclass, asdict, MISSING
from typing import Any, get_origin, get_args
from collections import defaultdict

from .field_meta import FieldMeta
from .schema_field import SchemaField


@dataclass
class Schema:
    groups: dict[str, list[SchemaField]]
    fields: list[SchemaField]


def group_fields(fields: list[SchemaField]) -> dict[str, list[SchemaField]]:
    groups = defaultdict(list)
    for field in fields:
        groups[field.meta.group].append(field)
    return dict(groups)


def build_fields(obj: Any) -> list[SchemaField]:
    fl: list[SchemaField] = []

    if not is_dataclass(obj):
        return fl

    is_instance = not isinstance(obj, type)

    for f in fields(obj):
        if is_instance:
            value = getattr(obj, f.name)
        else:
            if f.default is not MISSING:
                value = f.default
            elif f.default_factory is not MISSING:
                value = f.default_factory()
            else:
                value = None

        sf = SchemaField.from_field(f, value=value)
        fl.append(sf)

    return fl


def schema(obj: Any) -> Schema:
    fields = build_fields(obj)
    groups = group_fields(fields)

    return Schema(
        fields=fields,
        groups=groups,
    )
