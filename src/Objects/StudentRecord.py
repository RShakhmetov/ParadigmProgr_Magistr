import Student
import Grade
import Course
import csv
import json
import os

class StudentRecord:

    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = []

    def add_student(self, student: Student):
        if student.student_id in self.students:
            raise ValueError("Студент с таким ID уже существует.")
        self.students[student.student_id] = student

    def add_course(self, course: Course):
        if course.course_id in self.courses:
            raise ValueError("Курс с таким ID уже существует.")
        self.courses[course.course_id] = course

    def add_grade(self, grade: Grade):
        if grade.student.student_id not in self.students:
            raise ValueError("Студент не найден в системе.")
        if grade.course.course_id not in self.courses:
            raise ValueError("Курс не найден в системе.")
        self.grades.append(grade)

    def remove_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Студент не найден.")

        del self.students[student_id]
        self.grades = [g for g in self.grades if g.student.student_id != student_id]

    def remove_course(self, course_id):
        if course_id not in self.courses:
            raise ValueError("Курс не найден.")
        del self.courses[course_id]
        self.grades = [g for g in self.grades if g.course.course_id != course_id]

    def remove_grade(self, student_id, course_id):
        initial_len = len(self.grades)
        self.grades = [g for g in self.grades if
                       not (g.student.student_id == student_id and g.course.course_id == course_id)]
        if len(self.grades) == initial_len:
            raise ValueError("Оценка не найдена.")

    def find_student(self, query):
        query = query.lower()
        return [s for s in self.students.values() if
                query in s.name.lower() or query in s.surname.lower() or query == str(s.student_id)]

    def find_course(self, query):
        query = query.lower()
        return [c for c in self.courses.values() if query in c.name.lower() or query == str(c.course_id)]

    def get_student_average(self, student_id) -> float:
        student_grades = [g.score for g in self.grades if g.student.student_id == student_id]
        return sum(student_grades) / len(student_grades) if student_grades else 0.0

    def get_course_average(self, course_id) -> float:
        course_grades = [g.score for g in self.grades if g.course.course_id == course_id]
        return sum(course_grades) / len(course_grades) if course_grades else 0.0

    def get_top_5_students(self):
        averages = []
        for s_id, student in self.students.items():
            avg = self.get_student_average(s_id)
            if avg > 0:
                averages.append((avg, student))
        averages.sort(key=lambda x: x[0], reverse=True)
        return averages[:5]

    def save_to_json(self, filename="data.json"):
        data = {
            "students": [s.to_dict() for s in self.students.values()],
            "courses": [c.to_dict() for c in self.courses.values()],
            "grades": [g.to_dict() for g in self.grades]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_json(self, filename="data.json"):
        if not os.path.exists(filename):
            raise FileNotFoundError("Файл не найден.")
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.students.clear()
        self.courses.clear()
        self.grades.clear()

        for s in data.get("students", []):
            self.add_student(Student(**s))
        for c in data.get("courses", []):
            self.add_course(Course(**c))
        for g in data.get("grades", []):
            student = self.students.get(g["student_id"])
            course = self.courses.get(g["course_id"])
            if student and course:
                self.add_grade(Grade(student, course, g["score"], g["date"]))

    def export_grades_to_csv(self, filename="grades_export.csv"):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Student_ID", "Student_Name", "Course_ID", "Course_Name", "Score", "Date"])
            for g in self.grades:
                writer.writerow([g.student.student_id, f"{g.student.surname} {g.student.name}",
                                 g.course.course_id, g.course.name, g.score, g.date])