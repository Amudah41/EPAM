import pytest

from hw5.tasks.task52_save_original_info import custom_sum


def init_of_function_for_test():
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)


def test_my_decorator__doc__():

    init_of_function_for_test()
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_my_decorator__name__():

    init_of_function_for_test()
    assert custom_sum.__name__ == "custom_sum"


def test_my_decorator__original_func():

    init_of_function_for_test()
    without_print = custom_sum.__original_func
    # the result returns without printing
    without_print(1, 2, 3, 4)

    assert "<function custom_sum at" in custom_sum.__original_func.__repr__()
