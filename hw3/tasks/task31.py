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

import timeit
from typing import Callable


def cache(times: int) -> Callable:
    if times < 0:
        raise ValueError("times must be non-negative")

    def custom_hash(func: Callable, *args, **kwargs):
        def my_wrapper():

            if my_wrapper.count < times:
                my_wrapper.count += 1
                return my_wrapper.tmp
            my_wrapper.count = 1
            my_wrapper.tmp = func(*args, **kwargs)
            return my_wrapper.tmp

        my_wrapper.count = 0
        my_wrapper.tmp = func(*args, **kwargs)
        return my_wrapper

    return custom_hash


# @cache(times=3)
# def f():
#     return input('? ')

if __name__ == "__main__":
    ...
