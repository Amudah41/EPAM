"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""

from typing import List


def BinSearch(li: List[int], x: int):
    """бинарный поиск, возвращающий результат наличия элемента в листе"""
    if x > li[-1] or x < li[0]:  # если сумма изначально вне границ листа
        return False
    i = 0
    j = len(li)-1
    while i < j:
        m = int((i+j)/2)
        if x > li[m]:
            i = m+1
        else:
            j = m

    if li[j] == x:
        return True
    else:
        return False


def delete_elements(a: List[int], b: List[int], c: List[int], d: List[int]):
    """Удаление элементов листов, которые сильно больше/меньше остальных"""
    lists = {0: a, 1: b, 2: c, 3: d}
    right_side = [a[-1], b[-1], c[-1], d[-1]]
    left_side = [a[0], b[0], c[0], d[0]]

    local_sum = sum([a[-1], b[-1], c[-1], d[-1]])
    local_max = max(a[-1], b[-1], c[-1], d[-1])
    while local_sum - 2 * local_max < 0:
        lists.get(right_side.index(local_max)).pop()
        try:
            local_sum = sum([a[-1], b[-1], c[-1], d[-1]])
        except:
            return False
        local_max = max(a[-1], b[-1], c[-1], d[-1])
        right_side = [a[-1], b[-1], c[-1], d[-1]]

    local_min = min(left_side)
    local_sum = sum([a[0], b[0], c[0], d[0]])
    while sum(left_side) - 2 * local_min > 0:
        lists.get(left_side.index(local_min)).pop(0)
        try:
            local_sum = sum([a[0], b[0], c[0], d[0]])
        except:
            return False
        local_min = min(a[0], b[0], c[0], d[0])
        left_side = [a[0], b[0], c[0], d[0]]
    return True


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    count = 0
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    # удаление элементов, которые точно не могут участвовать в искомой сумме
    if not delete_elements(a, b, c, d):
        return 0
    for item1 in a:
        for item2 in b:
            tmp = item1 + item2
            for item3 in c:
                # поиск суммы трёх элементов с обратным знаком в листе d
                if BinSearch(d, -(tmp + item3)):
                    count += 1
    return count
