# Here's a not very efficient calculation function that calculates something important::

import hashlib
import random
import struct
import time
import timeit
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


# Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
# Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
# You are not allowed to modify slow_calculate function.


def pallelization(n: int) -> int:
    starttime = timeit.default_timer()
    with Pool(n) as p:
        sum(p.map(slow_calculate, range(501)))
    return timeit.default_timer() - starttime


"""
The caulculation time is 57.14936398999998, count of processes is: 20
The caulculation time is 21.239177954999832, count of processes is: 60
The caulculation time is 7.007313468000575, count of processes is: 240
"""
