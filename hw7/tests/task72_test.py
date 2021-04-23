import pytest

from hw7.tasks.task72 import yeild_str, backspace_compare
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
def test_yeild_str(input_str: str, expected_result: List[str]):
    actual_result = [item for item in yeild_str(input_str)]
    assert actual_result == expected_result


def test_positive_backspace_compare_with_example_value_1():
    assert backspace_compare(s="ab#c", t="ad#c") == True


def test_positive_backspace_compare_with_example_value_2():
    assert backspace_compare(s="a##c", t="#a#c") == True


def test_positive_backspace_compare_with_my_value():
    assert backspace_compare(s="ab", t="#a#c#c###s##c##ab") == True


def test_negative_backspace_compare_with_example_value():
    assert backspace_compare(s="a#c", t="b") == False


def test_negative_backspace_compare_with_empty_value():
    assert backspace_compare(s="a#c#", t="") == True
