import pytest
from hw3.tasks.task34 import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (9, True),
        (153, True),
        (10, False),
    ],
)
def test_is_armstrong(number: int, expected_result: bool):
    assert is_armstrong(number) is expected_result
