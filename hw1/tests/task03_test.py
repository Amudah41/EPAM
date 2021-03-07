import pytest
from typing import Tuple

from tasks.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("some_file1.txt", (-54,22)),
        ("some_file2.txt", (-54,7)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result