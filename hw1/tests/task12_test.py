import pytest
from hw1.tasks.task12 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2], True),
        ([0, 1, 1, 3], False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
