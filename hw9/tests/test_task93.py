import pytest
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock

import hw9
from hw9.tasks.task93 import universal_file_counter, count_from_file


def test_positive_count_from_file_without_tokenizer_mock():
    with patch("builtins.open", mock_open(read_data="1 2 3\n 4 \n 5 \n")) as mock_input:
        assert count_from_file("_.txt") == 3


def test_positive_count_from_file_with_tokenizer_mock():
    with patch("builtins.open", mock_open(read_data="1 2 3\n 4 \n 5 \n")) as mock_input:
        assert count_from_file("_.txt", str.split) == 5


@pytest.fixture()
def my_count_from_file(monkeypatch):
    mock = MagicMock()
    mock.return_value = 1

    monkeypatch.setattr(hw9.tasks.task93, "count_from_file", mock)


def test_correct_recognizing_py_files_in_directory(my_count_from_file):
    assert universal_file_counter(Path("hw9/tests"), "py") == 3


def test_correct_recognizing_txt_files_in_directory(my_count_from_file):
    assert universal_file_counter(Path("hw9/tests"), "txt") == 0
