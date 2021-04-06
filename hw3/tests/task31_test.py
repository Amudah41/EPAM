import timeit
from typing import Callable, List

import pytest
from hw3.tasks.task31 import cache


@pytest.mark.parametrize("count_times", [2, 3, 0])
def test_cache_good_working(count_times: int):
    @cache(times=count_times)
    def f():
        return timeit.default_timer()

    output = f()
    for i in range(count_times - 1):
        assert f() == output

    assert f() != output


def test_cache_bad_working():

    try:

        @cache(times=-1)
        def f():
            return timeit.default_timer()

    except:
        assert True
