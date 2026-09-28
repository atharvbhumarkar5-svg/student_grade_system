"""Input validation logic for IDs, names, and score boundaries."""

class ValidationError(Exception):
    pass

class Validator:
    @staticmethod
    def validate_student_id(student_id: str) -> str:
        clean_id = student_id.strip()
        if not clean_id or not clean_id.isalnum():
            raise ValidationError("Student ID must be alphanumeric and non-empty.")
        return clean_id.upper()

    @staticmethod
    def validate_name(name: str) -> str:
        clean_name = name.strip()
        if len(clean_name) < 2 or not all(part.isalpha() for part in clean_name.split()):
            raise ValidationError("Student name must contain alphabetical characters and be at least 2 letters.")
        return clean_name.title()

    @staticmethod
    def validate_score(score_str: str) -> float:
        try:
            score = float(score_str)
        except ValueError:
            raise ValidationError("Marks must be a valid numeric value.")
        if score < 0.0 or score > 100.0:
            raise ValidationError("Marks must be between 0.0 and 100.0.")
        return round(score, 2)