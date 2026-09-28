"""Evaluation module implementing standard academic scale conversion."""
from typing import Dict, Tuple

class GradeCalculator:
    # Scale: VIT/Standard 10-Point Relative/Absolute Grading
    GRADE_BOUNDS = [
        (90.0, "S", 10.0),
        (80.0, "A", 9.0),
        (70.0, "B", 8.0),
        (60.0, "C", 7.0),
        (50.0, "D", 6.0),
        (40.0, "E", 4.0),
        (0.0,  "F", 0.0)
    ]

    @classmethod
    def calculate_letter_grade(cls, score: float) -> Tuple[str, float]:
        for threshold, letter, gpa in cls.GRADE_BOUNDS:
            if score >= threshold:
                return letter, gpa
        return "F", 0.0

    @classmethod
    def compute_student_summary(cls, marks: Dict[str, float]) -> Dict[str, any]:
        if not marks:
            return {"average": 0.0, "letter": "N/A", "gpa": 0.0, "status": "No Courses"}

        avg = round(sum(marks.values()) / len(marks), 2)
        letter, gpa = cls.calculate_letter_grade(avg)
        status = "Passed" if letter != "F" else "Failed"
        return {"average": avg, "letter": letter, "gpa": gpa, "status": status}