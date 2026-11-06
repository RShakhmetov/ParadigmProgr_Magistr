import itertools

class Student:
    id_obj = itertools.count()

    def __init__(self, name, surname, birth_date, group):
        self.student_id = next(Student.id_obj)
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.group = group

    def get_info(self) -> dict:

        return {
            "ID": self.student_id,
            "Имя": self.name,
            "Фамилия": self.surname,
            "Дата рождения": self.birth_date,
            "Группа": self.group
        }

    def update(self, name = None, surname = None, birth_date= None, group = None):
        if name: self.name = name
        if surname: self.surname = surname
        if birth_date: self.birth_date = birth_date
        if group: self.group = group

    def to_dict(self) -> dict:

        return {
            "student_id": self.student_id,
            "name": self.name,
            "surname": self.surname,
            "birth_date": self.birth_date,
            "group": self.group
        }

    def __str__(self):
        return f"[{self.student_id}] {self.surname} {self.name} (Группа: {self.group})"

