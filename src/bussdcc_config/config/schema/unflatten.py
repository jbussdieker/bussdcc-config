from typing import Any
from .node import SchemaNode

from ..builder import _coerce


def unflatten(schema: SchemaNode, flat: dict[str, Any]) -> dict[str, Any]:
    def build(node: SchemaNode, prefix: str = "") -> dict[str, Any]:
        result: dict[str, Any] = {}

        node_prefix = prefix
        if node.name:
            node_prefix = f"{prefix}.{node.name}" if prefix else node.name

        # primitive fields
        for field in node.fields:
            key = f"{node_prefix}.{field.name}" if node_prefix else field.name
            value = flat.get(key, field.value)
            result[field.name] = _coerce(field.type, value)

        # nested dataclasses
        for child in node.children:
            if child.container is None:
                if child.name:
                    result[child.name] = build(child, node_prefix)
                else:
                    raise RuntimeError("Shouldn't happen")

            elif child.container == "list":
                list_items = []

                for item in child.items or []:
                    list_items.append(build(item, f"{node_prefix}.{item.name}"))

                if child.name:
                    result[child.name] = list_items
                else:
                    raise RuntimeError("Shouldn't happen")

            elif child.container == "dict":
                items = {}

                for item in child.items or []:
                    items[item.name] = build(item, f"{node_prefix}.{item.name}")

                if child.name:
                    result[child.name] = items
                else:
                    raise RuntimeError("Shouldn't happen")

        return result

    return build(schema)
