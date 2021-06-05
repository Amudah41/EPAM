import pytest

from hw7.tasks.task72 import backspaced_elemets_and_reverse_str, backspace_compare
from typing import List


@pytest.mark.parametrize(
    ["input_str", "expected_result"],
    [
        ("12345", ["5", "4", "3", "2", "1"]),
        ("#1###2#3#4##5", ["5"]),
        ("", []),
        ("###", []),
    ],
)
def test_backspaced_elemets_and_reverse_str(input_str: str, expected_result: List[str]):
    actual_result = [item for item in backspaced_elemets_and_reverse_str(input_str)]
    assert actual_result == expected_result


def test_positive_backspace_compare_with_example_value_1():
    assert backspace_compare(s="ab#c", t="ad#c")


def test_positive_backspace_compare_with_example_value_2():
    assert backspace_compare(s="a##c", t="#a#c")


def test_positive_backspace_compare_with_my_value():
    assert backspace_compare(s="ab", t="#a#c#c###s##c##ab")


def test_negative_backspace_compare_with_example_value():
    assert not backspace_compare(s="a#c", t="b")


def test_negative_backspace_compare_with_empty_value():
    assert backspace_compare(s="a#c#", t="")
