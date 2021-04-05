from typing import Any, Callable, List, Tuple

import pytest
from hw3.tasks.task33 import Filter, make_filter


@pytest.mark.parametrize(
    ["functions", "value", "expected_result"],
    [
        (
            (lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)),
            range(100),
            [i for i in range(2, 100, 2)],
        ),
    ],
)
def test_positive_even_produser(
    functions: Tuple[Callable], value: object, expected_result: List[int]
):
    positive_even = Filter(functions)
    assert positive_even.apply(range(100)) == expected_result


@pytest.mark.parametrize(
    ["sample_data", "keywords", "expected_result"],
    [
        (
            [
                {
                    "name": "Bill",
                    "last_name": "Gilbert",
                    "occupation": "was here",
                    "type": "person",
                },
                {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
            ],
            {"name": "polly", "type": "bird"},
            [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}],
        )
    ],
)
def test_second_entry_with_keywords_dict(
    sample_data: List[dict], keywords: dict, expected_result: List[dict]
):
    actual_result = make_filter(**keywords).apply(sample_data)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["sample_data", "expected_result"],
    [
        (
            [
                {
                    "name": "Bill",
                    "last_name": "Gilbert",
                    "occupation": "was here",
                    "type": "person",
                },
                {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
            ],
            [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}],
        )
    ],
)
def test_second_entry_with_keywords_manual_input(
    sample_data: List[dict],
    expected_result: List[dict],
):
    actual_result = make_filter(name="polly", type="bird").apply(sample_data)

    assert actual_result == expected_result
