"""result.py - the Result class and the sample grading scale."""

# SAMPLE grading scale (NOT an official university policy).
# A tuple of tuples: (minimum mark, grade). Checked from the top down.
# Change the numbers here to change grading everywhere in the program.
GRADE_SCALE = (
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
)

MIN_MARK = 0
MAX_MARK = 100


class Result:
    """One student's examination mark in one course."""

    def __init__(self, student_id, course_code, mark):
        self.student_id = student_id
        self.course_code = course_code
        self.mark = mark
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        """Instance method: work out the grade for THIS result's mark."""
        for minimum, grade in GRADE_SCALE:
            if self.mark >= minimum:
                return grade
        return "F"

    def display_info(self):
        """Print this result on one line."""
        print(f"  {self.student_id:<10} {self.course_code:<8} "
              f"{self.mark:>6.1f}   {self.grade}")

    @staticmethod
    def is_valid_mark(mark):
        """True if the mark is between 0 and 100 (inclusive)."""
        return MIN_MARK <= mark <= MAX_MARK
