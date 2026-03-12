from typing import Literal
from dataclasses import fields, is_dataclass, asdict
from typing import Any, get_origin, get_args
from collections import defaultdict

from .meta import FieldMeta


def group_schema(schema: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    groups = defaultdict(list)
    for field in schema:
        groups[field["group"]].append(field)
    return dict(groups)


def build_schema(obj: Any, prefix: str = "") -> list[dict[str, Any]]:
    schema: list[dict[str, Any]] = []
    if not is_dataclass(obj):
        return schema

    for f in fields(obj):
        value = getattr(obj, f.name)
        meta = FieldMeta.from_field(f)
        name = f"{prefix}.{f.name}" if prefix else f.name

        # nested dataclass
        if is_dataclass(value):
            schema.extend(build_schema(value, name))
            continue

        origin = get_origin(f.type)
        args = get_args(f.type)

        # dict[str, dataclass]
        if origin is dict and value:
            _, val_type = get_args(f.type)

            if is_dataclass(next(iter(value.values()), None)):
                for k, v in value.items():
                    schema.extend(build_schema(v, f"{name}.{k}"))
                continue

        ui = meta.ui
        options = None

        # Literal → select
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

        schema.append(
            {
                **asdict(meta),
                "name": name,
                "field": f.name,
                "ui": ui,
                "value": value,
                "type": f.type,
                "options": options,
            }
        )

    return schema
