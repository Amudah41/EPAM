"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']



"""
import string
from typing import Iterable, List
from warnings import warn


def custom_range(seq: Iterable[any], *args) -> List[any]:
    output = []
    if len(args) == 1:
        index = seq.index(args[0])
        for i in range(0, index):
            output.append(seq[i])
    elif len(args) == 2:
        start, finish = args
        index_start = seq.index(start)
        index_finish = seq.index(finish)
        for i in range(index_start, index_finish):
            output.append(seq[i])
    elif len(args) == 3:
        start, finish, custom_step = args
        index_start = seq.index(start)
        index_finish = seq.index(finish)
        for i in range(index_start, index_finish, custom_step):
            output.append(seq[i])
    else:
        raise Exception("Too many arguments for range!")
    return output
