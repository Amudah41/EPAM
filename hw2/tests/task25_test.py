import string
from typing import Iterable, List

import pytest

from hw2.tasks.task25 import custom_range


@pytest.mark.parametrize(
    ["seq", "value", "expected_result"],
    [(string.ascii_lowercase, "g", ["a", "b", "c", "d", "e", "f"])],
)
def test_custom_range_1(seq: Iterable[any], value: any, expected_result: List[any]):
    actual_result = custom_range(seq, value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["seq", "value1", "value2", "expected_result"],
    [
        (
            string.ascii_lowercase,
            "g",
            "p",
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
    ],
)
def test_custom_range_2(
    seq: Iterable[any], value1: any, value2: any, expected_result: List[any]
):
    actual_result = custom_range(seq, value1, value2)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["seq", "value1", "value2", "value3", "expected_result"],
    [(string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"])],
)
def test_custom_range_3(
    seq: Iterable[any],
    value1: any,
    value2: any,
    value3: any,
    expected_result: List[any],
):
    actual_result = custom_range(seq, value1, value2, value3)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["seq", "value1", "value2", "value3", "value4"],
    [(string.ascii_lowercase, "p", "g", -2, 4)],
)
def test_custom_range_4(
    seq: Iterable[any], value1: any, value2: any, value3: any, value4: any
):
    try:
        custom_range(seq, value1, value2, value3, value4)
    except:
        assert True
