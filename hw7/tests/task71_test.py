import pytest

from hw7.tasks.task71 import find_occurrences


def test_positive_for_example():
    example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "my_valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "my_value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "my_values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
    }

    assert find_occurrences(example_tree, "RED") == 6


def test_all_basic_structures():
    my_tree = {
        "first": [42, "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", 42, "my_valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": 42,
            "complex_key": {
                "key1": "my_value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "my_values", {"nested_key": 42}],
            },
        },
        "fourth": {1: 2, True: [False, 42]},
        "fifth": False,
    }

    assert find_occurrences(my_tree, 42) == 5
