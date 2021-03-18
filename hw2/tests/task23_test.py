from typing import Any, List, Tuple

import pytest

from hw2.tasks.task23 import combinations


@pytest.mark.parametrize(
    ["value1", "value2", "expected_result"],
    [
        ([1, 2], [3, 4], [[1, 3], [1, 4], [2, 3], [2, 4]]),
    ],
)
def test_combinations(
    value1: List[Any], value2: List[Any], expected_result: List[List]
):
    actual_result = combinations(value1, value2)

    assert actual_result == expected_result

@pytest.mark.parametrize(
    ["value1", "value2", "value3", "expected_result"],
    [
        (
            ["a", "b"],
            [1, 2, 3],
            [True],
            [
                ["a", 1, True],
                ["a", 2, True],
                ["a", 3, True],
                ["b", 1, True],
                ["b", 2, True],
                ["b", 3, True],
            ],
        ),
        (
            ["a", -1.23],
            [set("1234"), 1],
            [{"43": 1}, "g", [32, 22, 11]],
            [
                ["a", {"1", "4", "2", "3"}, {"43": 1}],
                ["a", {"1", "4", "2", "3"}, "g"],
                ["a", {"1", "4", "2", "3"}, [32, 22, 11]],
                ["a", 1, {"43": 1}],
                ["a", 1, "g"],
                ["a", 1, [32, 22, 11]],
                [-1.23, {"1", "4", "2", "3"}, {"43": 1}],
                [-1.23, {"1", "4", "2", "3"}, "g"],
                [-1.23, {"1", "4", "2", "3"}, [32, 22, 11]],
                [-1.23, 1, {"43": 1}],
                [-1.23, 1, "g"],
                [-1.23, 1, [32, 22, 11]],
            ],
        ),
    ],
)
def test_combinations(
    value1: List[Any], value2: List[Any], value3: List[Any], expected_result: List[List]
):
    actual_result = combinations(value1, value2, value3)

    assert actual_result == expected_result
