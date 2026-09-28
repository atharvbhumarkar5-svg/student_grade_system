"""CLI entrypoint for Student Grade Management System."""
import sys
from sgs.models import Student
from sgs.storage import StorageManager
from sgs.validator import Validator, ValidationError
from sgs.grade_calculator import GradeCalculator
from sgs.analytics import AnalyticsEngine

class Application:
    def __init__(self):
        self.storage = StorageManager()
        self.students = self.storage.load_all()

    def add_student(self):
        try:
            sid = Validator.validate_student_id(input("Enter Student ID: "))
            if sid in self.students:
                print(f"[!] Student {sid} already exists.")
                return
            name = Validator.validate_name(input("Enter Full Name: "))
            self.students[sid] = Student(student_id=sid, name=name)
            self.storage.save_all(self.students)
            print(f"[+] Record created for {name} ({sid}).")
        except ValidationError as err:
            print(f"Validation Error: {err}")

    def enter_marks(self):
        sid = input("Enter Student ID: ").strip().upper()
        if sid not in self.students:
            print("[!] Student ID not registered.")
            return
        subject = input("Enter Course/Subject Code: ").strip().upper()
        try:
            score = Validator.validate_score(input("Enter Score (0-100): "))
            self.students[sid].marks[subject] = score
            self.storage.save_all(self.students)
            print(f"[+] Score {score} logged for {sid} in {subject}.")
        except ValidationError as err:
            print(f"Validation Error: {err}")

    def view_report_card(self):
        sid = input("Enter Student ID: ").strip().upper()
        if sid not in self.students:
            print("[!] Student not found.")
            return
        s = self.students[sid]
        print(f"\n{'='*45}\nSTUDENT REPORT CARD\n{'='*45}")
        print(f"ID: {s.student_id:<15} Name: {s.name}")
        print(f"{'-'*45}\nSubject{' '*20}Score")
        print(f"{'-'*45}")
        for sub, score in s.marks.items():
            print(f"{sub:<25} {score:>6.2f}")
        summary = GradeCalculator.compute_student_summary(s.marks)
        print(f"{'-'*45}")
        print(f"Average: {summary['average']}% | Grade: {summary['letter']} | GPA: {summary['gpa']} | Status: {summary['status']}")
        print(f"{'='*45}\n")

    def display_all(self):
        if not self.students:
            print("[!] Registry is empty.")
            return
        print(f"\n{'ID':<12} {'Name':<20} {'Courses':<10} {'Average':<10} {'Grade'}")
        print("-" * 60)
        for s in self.students.values():
            summary = GradeCalculator.compute_student_summary(s.marks)
            print(f"{s.student_id:<12} {s.name:<20} {len(s.marks):<10} {summary['average']:<10.2f} {summary['letter']}")
        print("-" * 60)

    def display_analytics(self):
        engine = AnalyticsEngine(self.students)
        topper = engine.find_topper()
        dist = engine.grade_distribution()
        print(f"\n{'='*35}\nCLASS-WIDE ANALYTICS & INSIGHTS\n{'='*35}")
        print(f"Total Enrolled  : {len(self.students)}")
        print(f"Batch Average   : {engine.class_average():.2f}%")
        print(f"Academic Topper : {topper.name if topper else 'N/A'}")
        print("\nGrade Breakdown:")
        for grade, count in dist.items():
            print(f"  Grade {grade}: {'*' * count} ({count})")
        print(f"{'='*35}\n")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ").strip().upper()
        if sid in self.students:
            del self.students[sid]
            self.storage.save_all(self.students)
            print(f"[x] Successfully removed record {sid}.")
        else:
            print("[!] ID not found.")

    def run(self):
        actions = {
            "1": self.add_student,
            "2": self.enter_marks,
            "3": self.view_report_card,
            "4": self.display_all,
            "5": self.display_analytics,
            "6": self.delete_student,
            "7": sys.exit
        }
        while True:
            print("\n=== STUDENT GRADE MANAGEMENT SYSTEM ===")
            print("1. Add New Student Profile")
            print("2. Enter Subject Marks")
            print("3. Print Student Grade Card")
            print("4. Display All Student Summaries")
            print("5. View Cohort Analytics & Metrics")
            print("6. Remove Student Record")
            print("7. Exit System")
            choice = input("Select an option (1-7): ").strip()
            handler = actions.get(choice)
            if handler:
                if choice == "7":
                    print("Exiting application.")
                    handler(0)
                handler()
            else:
                print("[!] Invalid option. Enter numbers between 1 and 7.")

if __name__ == "__main__":
    Application().run()