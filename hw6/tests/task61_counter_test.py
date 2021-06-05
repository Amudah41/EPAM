import pytest

from hw6.tasks.task61_counter import instances_counter


@instances_counter
class User:
    pass


def test_count_of_initial_get_created_instanses():
    assert User.get_created_instances() == 0


def test_count_of_get_created_instanses_with_three_instance():
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3


def test_reset_instances_counter_correct_output():
    user_2 = User()
    assert user_2.reset_instances_counter() == 4


def test_correct_get_created_instanses_after_reset_instances_counter_():
    assert User.get_created_instances() == 0


@instances_counter
class OtherUser:
    pass


def test_correct_working_with_two_classes_before_reset_instances_counter():
    user, _, _ = User(), User(), User()
    other_user, _ = OtherUser(), OtherUser()
    assert other_user.get_created_instances() == 2


def test_correct_working_with_two_classes_after_reset_instances_counter():
    user, _, _ = User(), User(), User()
    user.reset_instances_counter()
    assert OtherUser.get_created_instances() == 2
