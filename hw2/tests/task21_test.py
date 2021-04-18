from typing import List

import pytest
from hw2.tasks.task21 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("./hw2/data1.txt", 35),
        ("./hw2/data2.txt", 2972),
    ],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    actual_result = count_non_ascii_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("./hw2/data1.txt", 43),
        ("./hw2/data2.txt", 5475),
    ],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    actual_result = count_punctuation_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (
            "./hw2/data1.txt",
            [
                "Gefährdung",
                "praktische",
                "ausführen",
                "überhaupt",
                "Forschung",
                "Natürlich",
                "handelt",
                "soziale",
                "glaubte",
                "solchen",
            ],
        ),
        (
            "./hw2/data2.txt",
            [
                "Nichtkämpfern",
                "verständlich",
                "kalyptischen",
                "Mobilmachung",
                "Umschreibung",
                "Zwickmühlen",
                "Verdichtung",
                "Soldatische",
                "übermächtig",
                "Schilderung",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("./hw2/data1.txt", "Ü"), ("./hw2/data2.txt", "›")],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    actual_result = get_rarest_char(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("./hw2/data1.txt", "ß"), ("./hw2/data2.txt", "ä")],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(file_path)

    assert actual_result == expected_result
