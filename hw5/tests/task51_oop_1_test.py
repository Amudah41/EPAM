import pytest
from datetime import datetime, timedelta

from hw5.tasks.task51_oop_1 import Homework, Student, Teacher


teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")
expired_homework = teacher.create_homework("Learn functions", 0)

create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)


def test_teacher_inits_works():
    assert teacher.last_name == "Daniil" and teacher.first_name == "Shadrin"


def test_student_inits_works():
    assert student.last_name == "Roman" and student.first_name == "Petrov"


def test_teacher_method_works():
    assert expired_homework.created.__class__ is datetime


def test_homework_deadline():
    assert str(expired_homework.deadline) == "0:00:00"


def test_homework_text():
    assert expired_homework.text == "Learn functions"


def test_oop_homework_deadline():
    assert str(oop_homework.deadline) == "5 days, 0:00:00"


def student_do_homework_oop_homework():
    assert student.do_homework(oop_homework) == oop_homework


def student_do_homework_expired_homework():
    student.do_homework(expired_homework)
    captured = capsys.readouterr()
    assert captured.out == "You are late"
