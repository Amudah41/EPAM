from unittest.mock import patch, mock_open
import pytest

from hw8.tasks.task81 import KeyValueStorage


def test_str_attribute():
    storage = KeyValueStorage("./hw8/task1.txt")
    assert storage.song == "shadilay"
    assert type(storage.song) is str


def test_int_attribute():
    storage = KeyValueStorage("./hw8/task1.txt")
    assert storage.power == 9001
    assert type(storage.power) is int


def test_valid_item_name():
    storage = KeyValueStorage("./hw8/task1.txt")
    assert storage["name"] == "kek"
    assert type(storage["name"]) is str


def test_not_valid_item_name():
    with patch("builtins.open", mock_open(read_data="1=smth")) as mock_input:
        with pytest.raises(
            ValueError, match="Value cannot be assigned to an attribute."
        ):
            KeyValueStorage("_.txt")
    assert True
