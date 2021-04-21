import timeit
from typing import Callable, List

import pytest
from hw3.tasks.task31 import cache


@pytest.mark.parametrize("count_times", [2, 3, 0])
def test_cache_good_working_without_args(count_times: int):
    @cache(times=count_times)
    def f():
        return timeit.default_timer()

    output = f()
    for i in range(count_times):
        assert f() == output

    assert f() != output


@pytest.mark.parametrize("count_times", [2, 3, 0])
def test_cache_good_working_with_one_group_of_args(count_times: int):
    @cache(times=count_times)
    def f(a, b, c):
        return timeit.default_timer()

    output = f(1, 2, 3)
    for i in range(count_times):
        assert f(1, 2, 3) == output

    assert f(1, 2, 3) != output


@pytest.mark.parametrize("count_times", [2, 3])
def test_cache_good_working_with_two_grous_of_args(count_times: int):
    @cache(times=count_times)
    def f(a, b, c):
        return timeit.default_timer()

    output_1 = f(1, 2, 3)
    output_2 = f(3, 4, 5)

    assert f(1, 2, 3) == output_1
    assert f(3, 4, 5) == output_2

    for i in range(count_times - 1):
        assert f(1, 2, 3) != f(3, 4, 5)

    assert f(1, 2, 3) != output_1
    assert f(3, 4, 5) != output_2


def test_cache_bad_value_of_times():
    with pytest.raises(ValueError, match="times must be non-negative"):

        @cache(times=-1)
        def f():
            ...

    assert True
