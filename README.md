# Student Learning and Examination Results Management System

PROG211 Object-Oriented Programming 1 - Individual Assignment
(Assignment title: *Real-World Solutions under DPG Standards*)
Domain: **Education** | Language: **Python 3.8+** (tested on 3.12) | No third-party packages

Author: `<YOUR NAME>` - Student No: `<YOUR STUDENT NUMBER>`

## 1. Overview and problem statement
Schools often record student marks on paper or in scattered spreadsheets, which causes
duplicate records, wrong marks and slow look-ups. This console program lets a user register
students and courses, record examination marks, and view results, grades and averages.

## 2. Objectives
- Apply classes, objects, attributes and constructors (Lecture 1).
- Store many objects in a Python **dictionary** (Lecture 2).
- Use **instance methods**, a **class method** (`@classmethod`) and a static method (Lecture 3).
- Follow the four Digital Public Goods (DPG) principles.

## 3. Intended users
Lecturers, exam officers and administrators of a small school or department.

## 4. Features
Register / view / search / update students; add courses; record results (marks 0-100);
view one student's results with average; view all results; summary statistics; input validation.

## 5. Requirements and setup
- Python 3.8 or newer (check with `python --version`). Nothing to install (`requirements.txt` lists no packages).

## 6. Running
```
cd student-results-management
python main.py            # start empty
python main.py --demo     # start with FICTIONAL sample data
```
(Use `python3` instead of `python` on Mac/Linux.) Type a number 1-10 and press Enter.

## 7. Example interaction (real output from this program)
```
Choose an option (1-10): 1
Student ID (e.g. STU001): STU010
Full name: Kadiatu Conteh
Programme (e.g. Diploma in IT): Diploma in IT
Student STU010 registered.

Choose an option (1-10): 6
Student ID: STU010
Course code: PROG211
Mark (0-100): 105
Mark must be between 0 and 100.

Choose an option (1-10): 6
Mark (0-100): 78.5
Result saved. Grade: B

Choose an option (1-10): 7
Results for Kadiatu Conteh:
  Student    Course     Mark   Grade
  STU010     PROG211    78.5   B
  Average mark: 78.5
```

## 8. Classes, objects, attributes, constructors
| Term | Meaning in this project |
|---|---|
| Class | A blueprint, e.g. `Student`, `Course`, `Result`, `ResultsManager` |
| Object | One real item made from a class, e.g. `Student("STU001", "Aminata Kamara", "Diploma in IT")` |
| Attribute | A variable belonging to an object (`name`) or the class (`total_students`) |
| Constructor | `__init__`, runs when an object is created and sets its attributes |
| Method | A function inside a class |

Object interaction: `ResultsManager` creates `Student`, `Course` and `Result` objects;
`Result` links a student ID to a course code; `Student.register_course()` is called when a result is saved.

## 9. Data structure chosen: dictionary
`self.students = {}` in `manager.py` stores `students[student_id] = Student object`.
Why: IDs are unique, so look-up is instant and duplicate IDs are easy to detect.
Courses use `{code: Course}`; results use `{(student_id, course_code): Result}`.
**Tuples (optional)**: used as dictionary keys for results (one result per student+course)
and for the `GRADE_SCALE` in `result.py`. They supplement, and do not replace, the dictionary.
Add/display functions: `ResultsManager.add_student()` and `display_all_students()`.

## 10. Methods
- **Instance methods** (take `self`, act on one object): `Student.display_info()`, `Student.update_details()`,
  `Student.register_course()`, `Result.calculate_grade()`, `Course.display_info()`.
- **Class method** (takes `cls`, acts on the class): `Student.get_total_students()` returns the class
  attribute `total_students`, which `__init__` increases. `Course.get_total_courses()` works the same way.
  Shown on menu option 9.
- **Static method** (no `self`/`cls`): `Student.is_valid_id()`, `Result.is_valid_mark()`. The brief's overview
  mentions static methods, so one is included as a bonus.
- Instance attribute = each object has its own copy (`name`). Class attribute = one shared copy (`total_students`).

## 11. DPG compliance (alignment only - not formal DPG certification)
1. **Open-source**: plain-text Python, MIT licence (`LICENSE`), published on GitHub (add your link below).
2. **Inclusive and accessible**: simple numbered menu, clear prompts, plain-language error messages, readable output, no colour or mouse needed.
3. **Privacy-respecting**: stores only student ID, name, programme, course codes and marks. No age, address, phone, ID numbers or passwords. All sample data is fictional. Nothing is written to disk.
4. **Modular and reusable**: separate files for each class; `manager.py` holds logic with no `input()` so it can be reused in another interface; `main.py` only handles the menu.

## 12. Grading scale (sample, not an official policy)
A 80-100, B 70-79, C 60-69, D 50-59, F 0-49. Edit `GRADE_SCALE` in `result.py` to change it.

## 13. Testing
`python -m unittest discover tests -v` - 16 automated tests, all passed when run on Python 3.12
(registration, duplicates, search, update, courses, valid/invalid marks, missing student/course,
duplicate result, grade/average, display, instance method, class method, invalid menu choice, exit).

## 14. Limitations
- Data lives in memory only and is **lost when the program closes**.
- Console only; single user; no login; sample grading scale.

## 15. Files
```
main.py  manager.py  student.py  course.py  result.py
tests/test_student_results.py   README.md   LICENSE   requirements.txt   .gitignore
screenshots/   (add your own screenshots here)
```

## 16. GitHub
Repository: `<PASTE YOUR GITHUB URL HERE>` - lecturer added as collaborator: `<fill in after you do it>`.

## 17. Authorship
Written for PROG211 at Limkokwing University of Creative Technology, Sierra Leone. `<Confirm in your own words what you wrote or adapted.>`
