class Student:
    def __init__(self, fio: str, group: str):
        self._fio = fio  # ФИО студента (строка)
        self._group = group  # группа (строка)
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark: int):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark: int):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio: str, subject: str):
        self._fio = fio
        self._subject = subject

    def set_mark(self, *args, **kwargs):
        raise NotImplementedError("В дочернем классе должен быть переопределен метод set_mark()")


class Lector(Mentor):
    """
    - для описания лекторов
    """

    @staticmethod
    def set_mark(student: Student, mark: int):
        student.add_lect_marks(mark=mark)

    def __str__(self):
        return "Лектор {}: предмет {}".format(self._fio, self._subject)


class Reviewer(Mentor):
    """
    - для описания экспертов
    """

    @staticmethod
    def set_mark(student: Student, mark):
        student.add_house_marks(mark=mark)

    def __str__(self):
        return "Эксперт {}: предмет {}".format(self._fio, self._subject)


if __name__ == "__main__":
    lector = Lector("Балакирев С.М.", "Информатика")
    reviewer = Reviewer("Гейтс Б.", "Информатика")
    students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
    persons = [lector, reviewer]
    lector.set_mark(students[0], 4)
    lector.set_mark(students[1], 2)
    reviewer.set_mark(students[0], 5)
    reviewer.set_mark(students[1], 3)
    for p in persons + students:
        print(p)

    # в консоли будет отображено:
    # Лектор Балакирев С.М.: предмет Информатика
    # Эксперт Гейтс Б.: предмет Информатика
    # Студент Иванов А.Б.: оценки на лекциях: [4]; оценки за д/з: [5]
    # Студент Гаврилов С.А.: оценки на лекциях: [2]; оценки за д/з: [3]
