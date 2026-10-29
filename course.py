"""course.py - the Course class."""


class Course:
    """Represents a course that students can sit an examination in."""

    total_courses = 0  # class attribute

    def __init__(self, course_code, title):
        self.course_code = course_code
        self.title = title
        Course.total_courses += 1

    def display_info(self):
        """Print this course's details (instance method)."""
        print(f"  Course Code: {self.course_code}")
        print(f"  Title      : {self.title}")

    @classmethod
    def get_total_courses(cls):
        """Return how many Course objects have been created."""
        return cls.total_courses
