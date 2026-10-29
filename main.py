"""main.py - menu-driven console interface.

Run with:   python main.py          (starts empty)
            python main.py --demo   (loads fictional sample data first)
"""

import sys
from manager import ResultsManager
from student import Student
from course import Course


def show_menu():
    print("\n===== STUDENT RESULTS MANAGEMENT SYSTEM =====")
    print(" 1. Register student")
    print(" 2. View all students")
    print(" 3. Search for a student")
    print(" 4. Update student details")
    print(" 5. Add course")
    print(" 6. Record examination result")
    print(" 7. View a student's results")
    print(" 8. View all examination results")
    print(" 9. Display summary statistics")
    print("10. Exit")


def ask(prompt):
    return input(prompt).strip()


def register_student(mgr):
    sid = ask("Student ID (e.g. STU001): ")
    name = ask("Full name: ")
    programme = ask("Programme (e.g. Diploma in IT): ")
    print(mgr.add_student(sid, name, programme)[1])


def search_student(mgr):
    student = mgr.find_student(ask("Enter student ID: "))
    if student:
        student.display_info()
    else:
        print("No student found with that ID.")


def update_student(mgr):
    sid = ask("Student ID to update: ")
    print("Leave a field blank to keep the old value.")
    name = ask("New name: ")
    programme = ask("New programme: ")
    print(mgr.update_student(sid, name, programme)[1])


def add_course(mgr):
    code = ask("Course code (e.g. PROG211): ")
    title = ask("Course title: ")
    print(mgr.add_course(code, title)[1])


def record_result(mgr):
    sid = ask("Student ID: ")
    code = ask("Course code: ")
    mark = ask("Mark (0-100): ")
    print(mgr.record_result(sid, code, mark)[1])


def print_result_table(results):
    print(f"  {'Student':<10} {'Course':<8} {'Mark':>6}   Grade")
    for result in results:
        result.display_info()


def view_student_results(mgr):
    sid = ask("Student ID: ")
    student = mgr.find_student(sid)
    if student is None:
        print("No student found with that ID.")
        return
    results = mgr.results_for_student(sid)
    if not results:
        print(f"{student.name} has no results yet.")
        return
    print(f"Results for {student.name}:")
    print_result_table(results)
    print(f"  Average mark: {mgr.average_for_student(sid):.1f}")


def view_all_results(mgr):
    if not mgr.results:
        print("No results recorded yet.")
    else:
        print_result_table(mgr.results.values())


def show_statistics(mgr):
    s = mgr.statistics()
    print(f"  Students registered : {s['students']}")
    print(f"  Courses available   : {s['courses']}")
    print(f"  Results recorded    : {s['results']}")
    if s["average"] is not None:
        print(f"  Average mark        : {s['average']:.1f}")
        print(f"  Highest / Lowest    : {s['highest']:.1f} / {s['lowest']:.1f}")
    print(f"  Student objects created (class method): "
          f"{Student.get_total_students()}")
    print(f"  Course objects created  (class method): "
          f"{Course.get_total_courses()}")


def main():
    mgr = ResultsManager()
    if "--demo" in sys.argv:
        mgr.load_demo_data()
        print("Demo data (fictional) loaded.")
    print("Note: records are kept in memory only and are lost on exit.")

    actions = {
        "1": register_student,
        "2": lambda m: m.display_all_students(),
        "3": search_student,
        "4": update_student,
        "5": add_course,
        "6": record_result,
        "7": view_student_results,
        "8": view_all_results,
        "9": show_statistics,
    }
    while True:
        show_menu()
        try:
            choice = ask("Choose an option (1-10): ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if choice == "10":
            print("Goodbye! (Remember: records were not saved.)")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please type a number from 1 to 10.")
        else:
            action(mgr)


if __name__ == "__main__":
    main()
