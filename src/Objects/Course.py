import itertools

class Course:
    id_obj = itertools.count()

    def __init__(self, name, teacher):
        self.course_id = next(Course.id_obj)
        self.name = name
        self.teacher = teacher

    def get_info(self):
        return {
            "ID": self.course_id,
            "Название": self.name,
            "Преподаватель": self.teacher
        }

    def update(self, name= None, teacher = None):
        if name: self.name = name
        if teacher: self.teacher = teacher

    def to_dict(self) -> dict:
        return {
            "course_id": self.course_id,
            "name": self.name,
            "teacher": self.teacher
        }

    def __str__(self):
        return f"[{self.course_id}] {self.name} (Преподаватель: {self.teacher})"