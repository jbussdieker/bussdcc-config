from dataclasses import is_dataclass, fields, MISSING
from typing import Tuple, Any, get_origin, get_args
from collections import defaultdict

from .node import SchemaNode
from .field import SchemaField


def _detect_container(tp: object) -> Tuple[str | None, Any | None]:
    origin = get_origin(tp)
    args = get_args(tp)

    if origin in (list, tuple) and args:
        item_tp = args[0]
        if len(args) == 2 and args[1] is Ellipsis:
            item_tp = args[0]

        if is_dataclass(item_tp):
            return "list", item_tp

    if origin is dict and len(args) == 2 and args[0] is str and is_dataclass(args[1]):
        return "dict", args[1]

    return None, None


def build(obj: Any, name: str | None = None) -> SchemaNode:
    if not is_dataclass(obj):
        raise TypeError("Expected dataclass")

    is_instance = not isinstance(obj, type)

    node_fields = []
    node_children = []

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

        container, subtype = _detect_container(f.type)

        # list[dataclass]
        if container == "list":
            items = []

            if value:
                for i, item in enumerate(value):
                    items.append(build(item, str(i)))

            prototype = build(subtype, None)

            node_children.append(
                SchemaNode(
                    name=f.name,
                    fields=[],
                    children=[],
                    container="list",
                    items=items,
                    item_schema=prototype,
                )
            )
            continue

        # dict[str, dataclass]
        if container == "dict":
            items = []

            if value:
                for k, v in value.items():
                    items.append(build(v, k))

            prototype = build(subtype, None)

            node_children.append(
                SchemaNode(
                    name=f.name,
                    fields=[],
                    children=[],
                    container="dict",
                    items=items,
                    item_schema=prototype,
                )
            )
            continue

        # nested dataclass
        if is_dataclass(f.type):
            nested = value if is_instance else f.type
            node_children.append(build(nested, f.name))
            continue

        # primitive field
        node_fields.append(
            SchemaField.from_field(
                f,
                value=value,
            )
        )

    return SchemaNode(
        name=name,
        fields=node_fields,
        children=node_children,
    )
