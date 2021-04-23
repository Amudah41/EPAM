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


def backspaced_elemets_and_reverse_str(my_str: str):
    my_str = iter(reversed(my_str))
    for a in my_str:
        if a == "#":
            try:
                next_item = next(my_str)
                while next_item == "#":
                    next_item = next(my_str)
            except StopIteration:
                break
            continue
        yield a


def backspace_compare(s: str = "", t: str = "") -> bool:
    return all(
        (
            first_str_letter == second_str_letter
            for first_str_letter, second_str_letter in zip_longest(
                backspaced_elemets_and_reverse_str(s),
                backspaced_elemets_and_reverse_str(t),
            )
        )
    )


if __name__ == "__main__":
    ...
