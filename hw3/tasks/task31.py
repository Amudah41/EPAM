# .. In previous homework task 4, you wrote a cache function that remembers other function output value.
# .. Modify it to be a parametrized decorator, so that the following code::

# ..     @cache(times=3)
# ..     def some_function():
# ..         pass

# .. Would give out cached value up to `times` number only.
# .. Example::

# ..     @cache(times=2)
# ..     def f():
# ..         return input('? ')   # careful with input() in python2, use raw_input() instead

# ..     >>> f()
# ..     ? 1
# ..     '1'
# ..     >>> f()     # will remember previous value
# ..     '1'
# ..     >>> f()     # but use it up to two times only
# ..     '1'
# ..     >>> f()
# ..     ? 2
# ..     '2'

from typing import Callable
from collections import defaultdict


def cache(times: int) -> Callable:
    if times < 0:
        raise ValueError("times must be non-negative")

    def custom_hash(func: Callable):
        log = defaultdict(list)

        def my_wrapper(*args, **kwargs):
            if times == 0:
                return func(*args, **kwargs)
            if not args in log:
                log[args].append(1)
                log[args].append(func(*args, **kwargs))
                return log[args][1]
            if log[args][0] < times:
                log[args][0] += 1
                return log[args][1]
            return log.pop(args)[1]

        return my_wrapper

    return custom_hash


# @cache(times=1)
# def f():
#     return input('? ')


if __name__ == "__main__":
    ...
