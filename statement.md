# Problem Statement: Student Grade Management System (SGS)

## 1. Problem Statement
Academic institutions require a consistent, error-free system to log student marks, convert them into institutional letter grades, compute GPA metrics, and generate batch performance analytics without manual calculation discrepancies.

## 2. Scope
The Student Grade System (SGS) is a modular terminal application featuring persistent JSON storage. It provides CRUD functionality for student academic records, robust input boundary checks, and batch statistical profiling.

## 3. Target Users
- Course Instructors and Professors
- Academic Administrators
- Department Program Chairs

## 4. High-Level Features
- Registration of student entities with unique ID validation.
- Course score entry with numeric bounds checks (0-100).
- Academic GPA and letter grade mapping.
- Cohort analytics: class averages, grade distributions, and batch topper identification.
- Atomic file-based persistence for cross-session data durability.