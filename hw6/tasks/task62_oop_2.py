"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Union


class Homework:
    def __init__(self, text: str, deadline: datetime) -> None:
        self.text = text
        self.deadline = timedelta(deadline)
        self.created = datetime.today()

    def is_active(self) -> bool:
        return datetime.today() - self.created < self.deadline


class DeadlineError(ValueError):
    def __init__(self, exception, message="You are late") -> None:
        self.exception = exception
        self.message = message


class Human:
    def __init__(self, last_name: str, first_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name


class Student(Human):
    def do_homework(self, student_homework: Homework, solution: str) -> "Homework":
        if not student_homework.is_active():
            raise DeadlineError("You are late")
        return HomeworkResult(self, student_homework, solution)


class HomeworkResult:
    def __init__(self, author: Student, homework: Homework, solution: str) -> None:
        if not homework.__class__ is Homework:
            raise ValueError("You gave a not Homework object")
        self.homework = homework
        self.author = author
        self.solution = solution
        self.created = homework.created


class Teacher(Human):
    homework_done = defaultdict(set)

    @staticmethod
    def check_homework(homework_result: HomeworkResult) -> bool:
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @staticmethod
    def reset_results(homework: Homework = None) -> None:
        if homework == None:
            Teacher.homework_done.clear()
        elif not homework in Teacher.homework_done:
            raise KeyError("There is not such homework in homework_done")
        else:
            Teacher.homework_done.pop(homework)

    @staticmethod
    def create_homework(homework_text: str, days: int) -> Homework:
        return Homework(homework_text, days)


if __name__ == "__main__":
    ...
