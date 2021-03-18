from typing import List, Tuple

import pytest

from hw2.tasks.task22 import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([3, 2, 3], 3, 2),
        ([2, 2, 1, 1, 1, 2, 2], 2, 1),
    ],
)
def major_and_minor_elem(value: List[int], expected_result: Tuple[int]):
    actual_result = major_and_minor_elem(value)

    assert actual_result == expected_result
