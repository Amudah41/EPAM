from typing import List, Tuple

import pytest
from hw3.tasks.task32 import pallelization


@pytest.mark.parametrize(
    ["count_of_processes", "time_limit"],
    [
        (30, 60),
        (60, 60),
        (160, 60),
    ],
)
@pytest.mark.skip
def test_pallelization(count_of_processes: int, time_limit: int):
    actual_result = pallelization(count_of_processes)

    assert actual_result <= time_limit
