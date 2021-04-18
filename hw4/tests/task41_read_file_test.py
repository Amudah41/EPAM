from typing import Callable, List
from unittest.mock import MagicMock, patch

import pytest

import hw4
from hw4.tasks.task41_read_file import (
    file_producer,
    is_useful_number,
    read_magic_number_only_value_error,
)


@pytest.mark.parametrize("number", [1, 2, 2.95])
def test_is_useful_number_positive_test(number: int):
    assert is_useful_number(number) == True


@pytest.mark.parametrize("number", [0, 3, 0.95])
def test_is_useful_number_negative_test(number: int):
    assert is_useful_number(number) == False


def test_read_magic_number_only_value_error_positive_test():
    assert (
        read_magic_number_only_value_error("hw4/tests/task41_test_positive.txt") == True
    )


def test_read_magic_number_only_value_error_negative_test():
    assert (
        read_magic_number_only_value_error("hw4/tests/task41_test_negative.txt")
        == False
    )


def test_read_magic_number_only_value_error_value_error_test():
    with pytest.raises(ValueError, match="Somthing came wrong."):

        read_magic_number_only_value_error("hw4/tests/task41_test_value_error.txt")

    assert True


def test_read_magic_number_only_value_error_file_error_test():
    with pytest.raises(ValueError, match="Somthing came wrong."):

        read_magic_number_only_value_error("hw4/tests/do_not_exist.txt")

    assert True


@pytest.mark.parametrize(
    ["text", "expected_result"],
    [["2", "2"], ["vfd dfv dd", "vfd dfv dd"], ["2 \n cd \n cdcs\n", "2"]],
)
def test_file_producer(text, expected_result):
    def readline_function(file: str):
        return open(file, "r").readline().strip()

    assert file_producer(text)(readline_function) == expected_result


# @pytest.fixture()
# def my_path(monkeypatch):
#     mock = MagicMock()
#     mock.return_value.readline.return_value = '2'

#     monkeypatch.setattr(
#         hw4.tasks.task41_read_file,
#         "open",
#         mock
#     )


# def test_read_magic_number_all_exceptions_positive_test(my_path):
#     assert read_magic_number_all_exceptions(my_path) == True
