"""student.py - the Student class.

A Student stores only basic, non-sensitive information (ID, name, programme)
so the project respects the "privacy-respecting" DPG principle.
"""


class Student:
    """Represents one student.

    Class attribute (shared by ALL students):
        total_students -- how many Student objects have been created.

    Instance attributes (each student has their own copy):
        student_id, name, programme, registered_courses
    """

    # Class attribute: belongs to the class itself, not to one object.
    total_students = 0

    def __init__(self, student_id, name, programme):
        """Constructor: runs automatically when Student(...) is called."""
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.registered_courses = []  # list of course codes
        Student.total_students += 1   # update the shared counter

    # ---------- INSTANCE METHODS (use `self`, work on ONE student) ----------
    def display_info(self):
        """Print this student's details."""
        courses = ", ".join(self.registered_courses) or "None yet"
        print(f"  Student ID : {self.student_id}")
        print(f"  Name       : {self.name}")
        print(f"  Programme  : {self.programme}")
        print(f"  Courses    : {courses}")

    def update_details(self, name=None, programme=None):
        """Change this student's name and/or programme.

        Blank values are ignored, so the old value is kept.
        Returns True if anything changed, otherwise False.
        """
        changed = False
        if name and name.strip():
            self.name = name.strip()
            changed = True
        if programme and programme.strip():
            self.programme = programme.strip()
            changed = True
        return changed

    def register_course(self, course_code):
        """Add a course code to this student (no duplicates)."""
        if course_code in self.registered_courses:
            return False
        self.registered_courses.append(course_code)
        return True

    # ---------- CLASS METHOD (uses `cls`, works on the whole class) ----------
    @classmethod
    def get_total_students(cls):
        """Return how many Student objects have been created so far."""
        return cls.total_students

    # ---------- STATIC METHOD (no self / cls; a plain helper) ----------
    @staticmethod
    def is_valid_id(student_id):
        """A valid ID is 3-12 letters, digits or hyphens, e.g. 'STU001'."""
        allowed = student_id.replace("-", "")
        return 3 <= len(student_id) <= 12 and allowed.isalnum()
