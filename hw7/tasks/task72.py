"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest


def yeild_str(my_str: str):
    my_str = iter(reversed(my_str))
    for a in my_str:
        if a == "#":
            try:
                _ = next(my_str)
                while _ == "#":
                    _ = next(my_str)
            except StopIteration:
                break
            continue
        print(a, my_str)
        yield a


def backspace_compare(s: str = "", t: str = "") -> bool:
    return all(
        (
            first_str_letter == second_str_letter
            for first_str_letter, second_str_letter in zip_longest(
                yeild_str(s), yeild_str(t)
            )
        )
    )


if __name__ == "__main__":
    ...
