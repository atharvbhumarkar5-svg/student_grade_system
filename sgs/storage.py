"""Persistence layer handling JSON operations and file locking/integrity."""
import json
import os
from typing import Dict
from sgs.models import Student

class StorageManager:
    def __init__(self, filepath: str = "data/students.json"):
        self.filepath = filepath
        self._ensure_file()

    def _ensure_file(self) -> None:
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def load_all(self) -> Dict[str, Student]:
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                return {sid: Student.from_dict(val) for sid, val in raw_data.items()}
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def save_all(self, registry: Dict[str, Student]) -> None:
        serialized = {sid: student.to_dict() for sid, student in registry.items()}
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(serialized, f, indent=4)