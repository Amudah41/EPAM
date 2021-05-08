import pytest
from unittest import mock
from hw9.tasks.task91 import merge_sorted_files, value_from_file, pase
from unittest.mock import patch, mock_open, MagicMock
import hw9


def test_for_examples_files():
    assert list(merge_sorted_files(["./hw9/file1.txt", "./hw9/file2.txt"])) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]


def test_for_3_files():
    assert list(
        merge_sorted_files(["./hw9/file1.txt", "./hw9/file2.txt", "./hw9/file3.txt"])
    ) == [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]


def test_without_files():
    assert list(merge_sorted_files([])) == []


def test_positive_int_value_from_file():
    my_file = MagicMock()
    my_file.readline.return_value = "2"
    assert value_from_file(my_file) == (True, 2)


def test_negative_not_int_value_from_file():
    my_file = MagicMock()
    my_file.readline.return_value = "smth"
    assert value_from_file(my_file) == (False, None)


@pytest.mark.parametrize(
    ["buffer", "index", "value", "expected_result"],
    [
        ([], 1, 0, [[1, 0]]),
        ([[1, 1], [2, 0]], 3, -1, [[1, 1], [2, 0], [3, -1]]),
        ([[1, 1], [2, 0]], 3, 2, [[3, 2], [1, 1], [2, 0]]),
        ([[1, 1], [2, -1]], 3, 0, [[1, 1], [3, 0], [2, -1]]),
    ],
)
def test_pase(buffer, index, value, expected_result):
    pase(buffer, index, value)
    assert buffer == expected_result
