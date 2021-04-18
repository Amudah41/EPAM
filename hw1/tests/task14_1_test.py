from typing import List

import pytest

from hw1.tasks.task14_1 import check_sum_of_four


@pytest.mark.parametrize(
    ["value1", "value2", "value3", "value4", "expected_result"],
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0),
        (
            [1, 2, 3, -6, -5, 0],
            [1, 2, -1, -4, 34, 5],
            [1, 2, 3, 4, 5, 6],
            [0, 0, -4, 6, -2, 78],
            51,
        ),
    ],
)
def test_check_sum_of_four(
    value1: List[int],
    value2: List[int],
    value3: List[int],
    value4: List[int],
    expected_result: int,
):
    actual_result = check_sum_of_four(value1, value2, value3, value4)

    assert actual_result == expected_result
