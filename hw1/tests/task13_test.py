from typing import Tuple

import pytest
from hw1.tasks.task13 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("./hw1/some_file1.txt", (-54, 22)),
        ("./hw1/some_file2.txt", (-54, 7)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
