from dataclasses import dataclass
from typing import Any

from .field import SchemaField


@dataclass(slots=True, frozen=True)
class SchemaNode:
    name: str | None
    fields: list[SchemaField]
    children: list["SchemaNode"]
    container: str | None = None
    items: list["SchemaNode"] | None = None
