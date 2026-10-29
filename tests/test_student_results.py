"""Automated tests. Run from the project folder:  python -m unittest discover tests -v"""
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from manager import ResultsManager
from student import Student
from result import Result
import main


def fresh():
    m = ResultsManager()
    m.add_student("STU001", "Test One", "IT")
    m.add_course("PROG211", "OOP 1")
    return m


class TestStudents(unittest.TestCase):
    def test_register_and_multiple(self):
        m = ResultsManager()
        self.assertTrue(m.add_student("STU001", "A", "IT")[0])
        self.assertTrue(m.add_student("STU002", "B", "IT")[0])
        self.assertEqual(len(m.students), 2)

    def test_duplicate_rejected(self):
        m = fresh()
        ok, _ = m.add_student("stu001", "Other", "IT")
        self.assertFalse(ok)
        self.assertEqual(len(m.students), 1)

    def test_search(self):
        m = fresh()
        self.assertIsNotNone(m.find_student("stu001"))
        self.assertIsNone(m.find_student("NOPE"))

    def test_update(self):
        m = fresh()
        self.assertTrue(m.update_student("STU001", "New Name", "")[0])
        self.assertEqual(m.find_student("STU001").name, "New Name")
        self.assertEqual(m.find_student("STU001").programme, "IT")
        self.assertFalse(m.update_student("GHOST", "x", "y")[0])

    def test_invalid_id(self):
        self.assertFalse(ResultsManager().add_student("!!", "A", "IT")[0])


class TestResults(unittest.TestCase):
    def test_course_added(self):
        self.assertIn("PROG211", fresh().courses)

    def test_valid_result(self):
        m = fresh()
        self.assertTrue(m.record_result("STU001", "PROG211", "85")[0])

    def test_invalid_marks(self):
        m = fresh()
        for bad in ("-1", "101", "abc", ""):
            self.assertFalse(m.record_result("STU001", "PROG211", bad)[0], bad)
        self.assertEqual(len(m.results), 0)

    def test_missing_student_or_course(self):
        m = fresh()
        self.assertFalse(m.record_result("GHOST", "PROG211", 50)[0])
        self.assertFalse(m.record_result("STU001", "NOPE", 50)[0])

    def test_duplicate_result(self):
        m = fresh()
        m.record_result("STU001", "PROG211", 50)
        self.assertFalse(m.record_result("STU001", "PROG211", 60)[0])

    def test_grades_and_average(self):
        m = fresh()
        m.add_course("NET101", "Net")
        m.record_result("STU001", "PROG211", 80)
        m.record_result("STU001", "NET101", 60)
        self.assertEqual(m.average_for_student("STU001"), 70)
        self.assertEqual(Result("X", "Y", 80).grade, "A")
        self.assertEqual(Result("X", "Y", 79.9).grade, "B")
        self.assertEqual(Result("X", "Y", 49).grade, "F")
        self.assertEqual(Result("X", "Y", 0).grade, "F")

    def test_display_all(self):
        m = ResultsManager()
        m.load_demo_data()
        with patch("sys.stdout", new=StringIO()) as out:
            m.display_all_students()
        self.assertIn("Aminata Kamara", out.getvalue())
        self.assertEqual(len(m.results), 4)


class TestMethods(unittest.TestCase):
    def test_instance_methods(self):
        s = Student("STU9", "Name", "IT")
        self.assertTrue(s.update_details(name="New"))
        self.assertEqual(s.name, "New")
        self.assertTrue(s.register_course("C1"))
        self.assertFalse(s.register_course("C1"))

    def test_class_method_counter(self):
        before = Student.get_total_students()
        Student("A1X", "x", "y")
        Student("A2X", "x", "y")
        self.assertEqual(Student.get_total_students(), before + 2)


class TestMenu(unittest.TestCase):
    def run_menu(self, inputs):
        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new=StringIO()) as out:
            main.main()
        return out.getvalue()

    def test_invalid_choice_then_exit(self):
        text = self.run_menu(["99", "abc", "10"])
        self.assertIn("Invalid choice", text)
        self.assertIn("Goodbye", text)

    def test_full_flow(self):
        text = self.run_menu(["1", "STU001", "Test", "IT", "5", "PROG211", "OOP",
                              "6", "STU001", "PROG211", "75", "7", "STU001", "10"])
        self.assertIn("Grade: B", text)
        self.assertIn("Average mark: 75.0", text)


if __name__ == "__main__":
    unittest.main()
