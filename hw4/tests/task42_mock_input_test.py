from unittest.mock import MagicMock
from urllib.request import urlopen

import pytest

import hw4
from hw4.tasks.task42_mock_input import count_dots_on_i


@pytest.fixture()
def my_url(monkeypatch):
    mock = MagicMock()
    mock.return_value.read.return_value = "fooiii".encode()

    monkeypatch.setattr(hw4.tasks.task42_mock_input, "urlopen", mock)


def test_count_dots_on_i(my_url):
    assert count_dots_on_i("some_url") == 3
