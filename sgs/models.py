"""Data models for Student and Course records."""
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Student:
    student_id: str
    name: str
    marks: Dict[str, float] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            marks=data.get("marks", {})
        )