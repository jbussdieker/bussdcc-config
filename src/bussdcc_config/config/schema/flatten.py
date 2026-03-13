from typing import Iterator
from dataclasses import replace

from .node import SchemaNode
from .field import SchemaField


def flatten(node: SchemaNode, prefix: str = "") -> Iterator[SchemaField]:
    node_prefix = prefix

    if node.name:
        node_prefix = f"{prefix}.{node.name}" if prefix else node.name

    # primitive fields
    for field in node.fields:
        name = f"{node_prefix}.{field.name}" if node_prefix else field.name
        yield replace(field, name=name)

    # normal nested dataclasses
    for child in node.children:
        if child.container is None:
            yield from flatten(child, node_prefix)

        elif child.container == "list":
            for item in child.items or []:
                list_prefix = f"{node_prefix}.{item.name}"
                yield from flatten(item, list_prefix)

        elif child.container == "dict":
            for item in child.items or []:
                dict_prefix = f"{node_prefix}.{item.name}"
                yield from flatten(item, dict_prefix)
