import pytest
from datetime import datetime, timedelta

from hw6.tasks.task62_oop_2 import (
    Homework,
    DeadlineError,
    Student,
    HomeworkResult,
    Teacher,
)


opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)


def test_teacher_inits_works():
    assert opp_teacher.last_name == "Daniil" and opp_teacher.first_name == "Shadrin"


def test_student_inits_works():
    assert lazy_student.last_name == "Roman" and lazy_student.first_name == "Petrov"


def test_teacher_method_works():
    assert oop_hw.created.__class__ is datetime


def test_oop_homework_text():
    assert oop_hw.text == "Learn OOP"


def test_docs_homework_deadline():
    assert str(oop_hw.deadline) == "1 day, 0:00:00"


def test_student_do_not_active_homework():
    teacher = Teacher("_", "_")
    student = Student("_", "_")
    expired_homework = teacher.create_homework("_", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(expired_homework, "some_solution")
    assert True


def test_HomeworkResult_with_ValueError_for_homework():
    with pytest.raises(ValueError, match="You gave a not Homework object"):
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    assert True


result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_positive_return_value_of_do_homework_is_HomeworkResult():
    assert result_1.__class__ is HomeworkResult


def test_available_homework_done_for_all_teachers():
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_positive_results_of_checking_oop_hws():

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    for res in Teacher.homework_done[oop_hw]:
        assert res.solution == "I have done this hw"


def test_positive_results_of_checking_docs_hws():

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    for res in Teacher.homework_done[docs_hw]:
        assert res.solution == "I have done this hw too"


def test_saving_docs_hw_results_after_reset_results_of_oop_hw():
    Teacher.reset_results(oop_hw)
    assert Teacher.homework_done[oop_hw] == set()
    for res in Teacher.homework_done[docs_hw]:
        assert res.solution == "I have done this hw too"


def test_positive_results_of_checking_hws_after_reset_all_results():

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    for res in Teacher.homework_done[oop_hw]:
        assert res.solution == "I have done this hw"
    for res in Teacher.homework_done[docs_hw]:
        assert res.solution == "I have done this hw too"
    Teacher.reset_results()
    for res in Teacher.homework_done[oop_hw]:
        assert res.solution == None
    for res in Teacher.homework_done[docs_hw]:
        assert res.solution == None


def test_reset_results_with_ValueError():
    with pytest.raises(ValueError, match="You can reset only Homework objects"):
        Teacher.reset_results("fff")
    assert True


def test_reset_results_with_KeyError():
    teacher = Teacher("_", "_")
    new_homework = teacher.create_homework("_", 10)
    with pytest.raises(KeyError, match="There is not such homework in homework_done"):
        Teacher.reset_results(new_homework)
    assert True
