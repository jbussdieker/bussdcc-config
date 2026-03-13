from typing import Iterable
from collections import defaultdict

from .field import SchemaField


def group(fields: Iterable[SchemaField]) -> dict[str, list[SchemaField]]:
    groups: dict[str, list[SchemaField]] = defaultdict(list)

    for field in fields:
        group = field.meta.group or "General"
        groups[group].append(field)

    return dict(groups)
