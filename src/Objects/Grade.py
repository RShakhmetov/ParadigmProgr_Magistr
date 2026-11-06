import Student
import Course

class Grade:
    def __init__(self, student: Student, course: Course, score, date):
        self.student = student
        self.course = course
        self.score = score
        self.date = date

    def get_info(self) -> dict:

        return {
            "Студент": f"{self.student.surname} {self.student.name}",
            "Курс": self.course.name,
            "Оценка": self.score,
            "Дата": self.date
        }

    def update(self, score = None, date = None):
        if score is not None: self.score = score
        if date: self.date = date

    def to_dict(self) -> dict:
        return {
            "student_id": self.student.student_id,
            "course_id": self.course.course_id,
            "score": self.score,
            "date": self.date
        }

    def __str__(self):
        return f"{self.student.surname} {self.student.name} | {self.course.name}: {self.score} ({self.date})"