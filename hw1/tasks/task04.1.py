"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""

import itertools
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    count = 0
    for point in itertools.product(a, b, c, d):
        if is_zero(point):
            count += 1
    return count


def is_zero(point: tuple):
    sum = 0
    for i in point:
        sum += i
    return sum == 0
