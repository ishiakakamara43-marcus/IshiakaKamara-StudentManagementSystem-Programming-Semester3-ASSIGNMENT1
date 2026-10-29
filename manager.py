"""manager.py - business logic (no input()/menus here, so it is reusable).

Data structures used (dictionaries):
    students : {student_id: Student}
    courses  : {course_code: Course}
    results  : {(student_id, course_code): Result}   <- tuple used as a key
"""

from student import Student
from course import Course
from result import Result


class ResultsManager:
    """Stores and manages all students, courses and results (in memory)."""

    def __init__(self):
        self.students = {}   # THE required dictionary: ID -> Student object
        self.courses = {}
        self.results = {}

    # ---------- students ----------
    def add_student(self, student_id, name, programme):
        """Create and store a Student. Returns (success, message)."""
        student_id = student_id.strip().upper()
        if not Student.is_valid_id(student_id):
            return False, "Invalid ID. Use 3-12 letters/digits, e.g. STU001."
        if not name.strip():
            return False, "Name cannot be empty."
        if student_id in self.students:
            return False, f"A student with ID {student_id} already exists."
        self.students[student_id] = Student(student_id, name.strip(),
                                            programme.strip() or "Not given")
        return True, f"Student {student_id} registered."

    def find_student(self, student_id):
        """Return the Student object, or None if not found."""
        return self.students.get(student_id.strip().upper())

    def update_student(self, student_id, name, programme):
        student = self.find_student(student_id)
        if student is None:
            return False, f"No student found with ID {student_id.upper()}."
        if student.update_details(name, programme):
            return True, "Student details updated."
        return False, "Nothing was changed."

    def display_all_students(self):
        """Loop through the dictionary and display every student."""
        if not self.students:
            print("  No students registered yet.")
            return
        for student in self.students.values():
            student.display_info()
            print("  " + "-" * 30)

    # ---------- courses ----------
    def add_course(self, course_code, title):
        course_code = course_code.strip().upper()
        if not course_code or not title.strip():
            return False, "Course code and title cannot be empty."
        if course_code in self.courses:
            return False, f"Course {course_code} already exists."
        self.courses[course_code] = Course(course_code, title.strip())
        return True, f"Course {course_code} added."

    # ---------- results ----------
    def record_result(self, student_id, course_code, mark):
        """Validate then store a Result. Returns (success, message)."""
        student_id = student_id.strip().upper()
        course_code = course_code.strip().upper()
        student = self.students.get(student_id)
        if student is None:
            return False, f"No student found with ID {student_id}."
        if course_code not in self.courses:
            return False, f"No course found with code {course_code}."
        try:
            mark = float(mark)
        except (TypeError, ValueError):
            return False, "Mark must be a number, e.g. 72.5."
        if not Result.is_valid_mark(mark):
            return False, "Mark must be between 0 and 100."
        key = (student_id, course_code)
        if key in self.results:
            return False, "A result for this student and course already exists."
        result = Result(student_id, course_code, mark)
        self.results[key] = result
        student.register_course(course_code)
        return True, f"Result saved. Grade: {result.grade}"

    def results_for_student(self, student_id):
        student_id = student_id.strip().upper()
        return [r for r in self.results.values() if r.student_id == student_id]

    def average_for_student(self, student_id):
        """Average mark for one student, or None if they have no results."""
        marks = [r.mark for r in self.results_for_student(student_id)]
        return sum(marks) / len(marks) if marks else None

    def statistics(self):
        """Return summary numbers as a dictionary."""
        marks = [r.mark for r in self.results.values()]
        return {
            "students": len(self.students),
            "courses": len(self.courses),
            "results": len(marks),
            "average": sum(marks) / len(marks) if marks else None,
            "highest": max(marks) if marks else None,
            "lowest": min(marks) if marks else None,
        }

    def load_demo_data(self):
        """Load FICTIONAL sample data for demonstration."""
        for sid, name, prog in (("STU001", "Aminata Kamara", "Diploma in IT"),
                                ("STU002", "Mohamed Sesay", "Diploma in IT"),
                                ("STU003", "Fatmata Bangura", "Diploma in IT")):
            self.add_student(sid, name, prog)
        self.add_course("PROG211", "Object-Oriented Programming 1")
        self.add_course("NET101", "Introduction to Networking")
        for sid, code, mark in (("STU001", "PROG211", 85), ("STU001", "NET101", 72),
                                ("STU002", "PROG211", 58), ("STU003", "PROG211", 45)):
            self.record_result(sid, code, mark)
