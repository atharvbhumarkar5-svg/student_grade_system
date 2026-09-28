"""Automated unit tests validating core logic."""
import unittest
from sgs.validator import Validator, ValidationError
from sgs.grade_calculator import GradeCalculator
from sgs.models import Student
from sgs.analytics import AnalyticsEngine

class TestStudentGradeSystem(unittest.TestCase):
    def test_validation_bounds(self):
        self.assertEqual(Validator.validate_score("89.5"), 89.5)
        with self.assertRaises(ValidationError):
            Validator.validate_score("105.0")
        with self.assertRaises(ValidationError):
            Validator.validate_score("-5")

    def test_grade_calculation(self):
        grade, gpa = GradeCalculator.calculate_letter_grade(92.0)
        self.assertEqual(grade, "S")
        self.assertEqual(gpa, 10.0)

        grade, gpa = GradeCalculator.calculate_letter_grade(38.0)
        self.assertEqual(grade, "F")
        self.assertEqual(gpa, 0.0)

    def test_analytics(self):
        s1 = Student("21BCE001", "Alice", {"Math": 95.0, "Physics": 85.0})
        s2 = Student("21BCE002", "Bob", {"Math": 60.0, "Physics": 70.0})
        engine = AnalyticsEngine({"21BCE001": s1, "21BCE002": s2})
        self.assertEqual(engine.class_average(), 77.5)
        self.assertEqual(engine.find_topper().name, "Alice")

if __name__ == "__main__":
    unittest.main()