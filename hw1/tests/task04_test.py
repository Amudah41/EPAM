import pytest
from typing import List

from tasks.task04 import BinSearch
from tasks.task04 import delete_elements
from tasks.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["value1", "value2", "expected_result"],
    [
        ([-11, 1, 2, 3, 4, 5, 11, 23], 1, True),
        ([2, 3, 4, 5, 1, -11, 23, 11], 1, False),
        ([2, 3, 4, 5, 1, -11, 23, 11], 0, False),
    ],
)
def test_BinSearch(value1: List[int], value2: int, expected_result: bool):
    actual_result = BinSearch(value1, value2)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value1", "value2", "value3", "value4", "expected_result"],
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [
         1, 2, 3, 4, 5], [1, 2, 3, 4, 5], False),
        ([1, 2, 3, -6, -5, 0], [1, 2, -1, -4, 34, 5],
         [1, 2, 3, 4, 5, 6], [0, 0, -4, 6, -2, 78], False),
        ([-6, -5, 0, 1, 2, 3], [-4, -1, 1, 2, 5, 34],
         [1, 2, 3, 4, 5, 6], [-4, -2, 0, 0, 6, 78], True),
    ],
)
def test_delete_elements(value1: List[int], value2: List[int], value3: List[int], value4: List[int], expected_result: bool):
    actual_result = delete_elements(value1, value2, value3, value4)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value1", "value2", "value3", "value4", "expected_result"],
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0),
        ([1, 2, 3, -6, -5, 0], [1, 2, -1, -4, 34, 5],
         [1, 2, 3, 4, 5, 6], [0, 0, -4, 6, -2, 78], 40),
    ],
)
def test_check_sum_of_four(value1: List[int], value2: List[int], value3: List[int], value4: List[int], expected_result: int):
    actual_result = check_sum_of_four(value1, value2, value3, value4)

    assert actual_result == expected_result
