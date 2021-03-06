from unittest.mock import patch, mock_open

import pytest

from hw4.tasks.task41_read_file import (
    file_producer,
    is_useful_number,
    read_magic_number_only_value_error,
)


@pytest.mark.parametrize("number", [1, 2, 2.95])
def test_is_useful_number_positive_test(number: int):
    assert is_useful_number(number)


@pytest.mark.parametrize("number", [0, 3, 0.95])
def test_is_useful_number_negative_test(number: int):
    assert not is_useful_number(number)


def test_read_magic_number_only_value_error_positive_test():
    assert read_magic_number_only_value_error("hw4/tests/task41_test_positive.txt")


def test_read_magic_number_only_value_error_negative_test():
    assert not read_magic_number_only_value_error("hw4/tests/task41_test_negative.txt")


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


def test_valid_item_name_in_range_with_mock():
    with patch("builtins.open", mock_open(read_data="1\n smth")) as mock_input:
        assert read_magic_number_only_value_error("_.txt")


def test_valid_item_name_not_in_range_with_mock():
    with patch("builtins.open", mock_open(read_data="6\n smth")) as mock_input:
        assert not read_magic_number_only_value_error("_.txt")


def test_not_valid_item_name_with_mock():
    with patch(
        "builtins.open", mock_open(read_data="smth_not_integer\n smth")
    ) as mock_input, pytest.raises(ValueError, match="Somthing came wrong."):
        assert read_magic_number_only_value_error("_.txt")
