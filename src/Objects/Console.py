import StudentRecord
import Student
import Grade
import Course

class ConsoleApp:
    def __init__(self):
        self.record = StudentRecord.StudentRecord()

    def print_menu(self):
        print("\n" + "=" * 40)
        print(" СИСТЕМА УЧЕТА СТУДЕНТОВ И ОЦЕНОК")
        print("=" * 40)
        print("1. Добавить студента")
        print("2. Добавить курс")
        print("3. Добавить оценку")
        print("4. Удалить студента")
        print("5. Удалить курс")
        print("6. Удалить оценку")
        print("7. Поиск студента/курса")
        print("8. Отчеты (Средние баллы, Топ-5)")
        print("9. Сохранить данные (JSON)")
        print("10. Загрузить данные (JSON)")
        print("11. Экспорт оценок в CSV")
        print("0. Выход")
        print("=" * 40)

    def run(self):
        while True:
            self.print_menu()
            choice = input("Выберите действие: ")

            try:
                if choice == '1':
                    self.add_student_ui()
                elif choice == '2':
                    self.add_course_ui()
                elif choice == '3':
                    self.add_grade_ui()
                elif choice == '4':
                    self.remove_student_ui()
                elif choice == '5':
                    self.remove_course_ui()
                elif choice == '6':
                    self.remove_grade_ui()
                elif choice == '7':
                    self.search_ui()
                elif choice == '8':
                    self.reports_ui()
                elif choice == '9':
                    self.record.save_to_json()
                    print("Данные успешно сохранены в data.json")
                elif choice == '10':
                    self.record.load_from_json()
                    print("Данные успешно загружены из data.json")
                elif choice == '11':
                    self.record.export_grades_to_csv()
                    print("Оценки успешно экспортированы в grades_export.csv")
                elif choice == '0':
                    print("Выход из программы. До свидания!")
                    break
                else:
                    print("Неверный пункт меню. Попробуйте снова.")
            except Exception as e:
                print(f"Ошибка: {e}")

    def add_student_ui(self):
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        b_date = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
        group = input("Введите группу: ")
        self.record.add_student(Student.Student(name, surname, b_date, group))
        print("Студент успешно добавлен.")

    def add_course_ui(self):
        name = input("Введите название курса: ")
        teacher = input("Введите ФИО преподавателя: ")
        self.record.add_course(Course.Course(name, teacher))
        print("Курс успешно добавлен.")

    def add_grade_ui(self):
        s_id = int(input("Введите ID студента: "))
        c_id = int(input("Введите ID курса: "))

        if s_id not in self.record.students or c_id not in self.record.courses:
            print("Студент или курс не найдены!")
            return

        score = float(input("Введите оценку (например, 4.5): "))
        date = input("Введите дату (ДД.ММ.ГГГГ): ")

        self.record.add_grade(Grade.Grade(self.record.students[s_id], self.record.courses[c_id], score, date))
        print("Оценка успешно добавлена.")

    def remove_student_ui(self):
        s_id = int(input("Введите ID студента для удаления: "))
        self.record.remove_student(s_id)
        print("Студент и его оценки удалены.")

    def remove_course_ui(self):
        c_id = int(input("Введите ID курса для удаления: "))
        self.record.remove_course(c_id)
        print("Курс и связанные оценки удалены.")

    def remove_grade_ui(self):
        s_id = int(input("Введите ID студента: "))
        c_id = int(input("Введите ID курса: "))
        self.record.remove_grade(s_id, c_id)
        print("Оценка удалена.")

    def search_ui(self):
        query = input("Введите ID или имя/фамилию для поиска: ")
        print("\n--- Результаты поиска (Студенты) ---")
        for s in self.record.find_student(query):
            print(s)

        print("\n--- Результаты поиска (Курсы) ---")
        for c in self.record.find_course(query):
            print(c)

    def reports_ui(self):
        print("\n--- ОТЧЕТЫ ---")
        s_id = input("Введите ID студента для среднего балла (или оставьте пустым): ")
        if s_id:
            try:
                avg = self.record.get_student_average(int(s_id))
                print(f"Средний балл студента: {avg:.2f}")
            except ValueError:
                print("Некорректный ID.")

        c_id = input("Введите ID курса для среднего балла (или оставьте пустым): ")
        if c_id:
            try:
                avg = self.record.get_course_average(int(c_id))
                print(f"Средний балл по курсу: {avg:.2f}")
            except ValueError:
                print("Некорректный ID.")

        print("\n--- ТОП-5 СТУДЕНТОВ ---")
        top = self.record.get_top_5_students()
        if not top:
            print("Нет данных об оценках.")
        for i, (avg, student) in enumerate(top, 1):
            print(f"{i}. {student.surname} {student.name} - Средний балл: {avg:.2f}")