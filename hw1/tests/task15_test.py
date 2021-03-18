from typing import List

import pytest

from hw1.tasks.task15 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value1", "value2", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1, -3, 5, 3, 6, 7], 4, 21),
    ],
)
def test_find_maximum_and_minimum(value1: List[int], value2: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(value1, value2)

    assert actual_result == expected_result
