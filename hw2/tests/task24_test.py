from typing import Callable, List, Tuple

import pytest

from hw2.tasks.task24 import cache


def func1(a, b):
    return (a ** b) ** 2


def func2(a, b, c):
    return a * b * c


@pytest.mark.parametrize(
    ["func", "some"],
    [
        (func1, (100, 200)),
        (func1, (200, 300)),
        (func2, (20, 30, 40)),
        (func2, (200, 300, 34)),
    ],
)
def test_cache(func: Callable, some: Tuple[int]):

    cache_func = cache(func)

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2
