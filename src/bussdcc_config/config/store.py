import json
from datetime import date, time, datetime
from typing import Any, Optional
from pathlib import Path

from bussdcc_framework import json as framework_json


class ConfigStore:
    def __init__(self, path: str | Path):
        if isinstance(path, str):
            path = Path(path)

        self.path = path
        self.data: Optional[dict[str, Any]] = {}

        if path.exists():
            self.data = framework_json.loads(path.read_text())
        else:
            self.data = None

    def save(self) -> None:
        if self.data is None:
            return

        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(framework_json.dumps(self.data, indent=2))
