import pytest
from unittest import mock
from hw9.tasks.task91 import merge_sorted_files
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
