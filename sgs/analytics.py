"""Statistical calculations and batch report generators."""
from typing import Dict, List, Optional
from sgs.models import Student
from sgs.grade_calculator import GradeCalculator

class AnalyticsEngine:
    def __init__(self, registry: Dict[str, Student]):
        self.registry = registry

    def class_average(self) -> float:
        if not self.registry:
            return 0.0
        scores = []
        for s in self.registry.values():
            if s.marks:
                scores.append(sum(s.marks.values()) / len(s.marks))
        return round(sum(scores) / len(scores), 2) if scores else 0.0

    def find_topper(self) -> Optional[Student]:
        if not self.registry:
            return None
        topper = None
        max_avg = -1.0
        for s in self.registry.values():
            if s.marks:
                avg = sum(s.marks.values()) / len(s.marks)
                if avg > max_avg:
                    max_avg = avg
                    topper = s
        return topper

    def grade_distribution(self) -> Dict[str, int]:
        distribution = {"S": 0, "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
        for s in self.registry.values():
            if s.marks:
                summary = GradeCalculator.compute_student_summary(s.marks)
                distribution[summary["letter"]] = distribution.get(summary["letter"], 0) + 1
        return distribution