"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    count = 0
    for item, my_value in tree.items():
        if item == element:
            count += 1

        def find_lists(my_value: Any):
            if my_value == element:
                nonlocal count
                count += 1
                return None
            if type(my_value) == dict:
                for subitem in my_value.values():
                    find_lists(subitem)
            if hasattr(my_value, "__iter__") and not type(my_value) is str:
                for subitem in my_value:
                    find_lists(subitem)

            return None

        find_lists(my_value)
    return count


if __name__ == "__main__":
    ...
