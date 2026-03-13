import json
from typing import Any, Optional
from pathlib import Path


class ConfigStore:
    def __init__(self, path: str | Path):
        if isinstance(path, str):
            path = Path(path)

        self.path = path
        self.data: Optional[dict[str, Any]] = {}

        if path.exists():
            self.data = json.loads(path.read_text())
        else:
            self.data = None

    def save(self) -> None:
        if self.data is None:
            return

        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2))
