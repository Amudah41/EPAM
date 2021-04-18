"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    log = {}

    def custom_hash(*args, **kwargs):
        if args in log:
            return log[args]
        log[args] = func(*args)
        return func(*args)

    return custom_hash


def func(a, b):
    return (a ** b) ** 2
