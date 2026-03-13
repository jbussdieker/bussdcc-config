from typing import Any, Type, get_origin, get_args, Literal
from dataclasses import is_dataclass, fields, MISSING
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import DataclassInstance


def _coerce(tp: Any, value: Any) -> Any:
    if value is None:
        return None

    if tp is bool:
        return value in ("on", "true", "1", True)

    if tp is int:
        return int(value)

    if tp is float:
        return float(value)

    return value


def build_dataclass(
    cls: DataclassInstance | type[DataclassInstance], data: dict[str, Any]
) -> Any:
    if not is_dataclass(cls):
        raise TypeError(f"{cls} is not a dataclass")

    kwargs = {}

    for f in fields(cls):
        value = data.get(f.name, MISSING)

        if value is MISSING:
            # use default if available
            if f.default is not MISSING:
                value = f.default
            elif f.default_factory is not MISSING:
                value = f.default_factory()
            else:
                value = None

        # detect nested dataclass
        if is_dataclass(f.type):
            value = build_dataclass(f.type, value or {})

        # detect list[dataclass]
        origin = get_origin(f.type)
        args = get_args(f.type)

        if origin is list and args and is_dataclass(args[0]) and value is not None:
            value = [build_dataclass(args[0], v) for v in value]

        # detect dict[str, dataclass]
        elif (
            origin is dict
            and args
            and args[0] is str
            and is_dataclass(args[1])
            and value is not None
        ):
            value = {k: build_dataclass(args[1], v) for k, v in value.items()}

        else:
            value = _coerce(f.type, value)

        kwargs[f.name] = value

    if isinstance(cls, type):
        return cls(**kwargs)
