"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz_1(n: int) -> List[str]:
    """
    >>> fizzbuzz_1(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz_1(16)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz', '16']
    >>> fizzbuzz_1(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> fizzbuzz_1(11.6)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """

    if type(n) != int:
        raise ValueError("n must be exact integer")

    if n <= 0:
        raise ValueError("n must be >= 0")

    buffer = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            buffer.append("fizz buzz")
        elif i % 3 == 0:
            buffer.append("fizz")
        elif i % 5 == 0:
            buffer.append("buzz")
        else:
            buffer.append(str(i))

    return buffer


def fizzbuzz_2(n: int) -> List[str]:
    """
    >>> fizzbuzz_2(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz_2(18)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz', '16', '17', 'fizz']
    >>> fizzbuzz_2(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> fizzbuzz_2(11.6)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """
    if type(n) != int:
        raise ValueError("n must be exact integer")

    if n <= 0:
        raise ValueError("n must be >= 0")

    buffer = []
    for i in range(1, n + 1):
        buffer.append(
            "fizz" * int(i % 3 == 0)
            + " " * int(i % 15 == 0)
            + "buzz" * int(i % 5 == 0)
            + str(i) * (i % 3 != 0 and i % 5 != 0)
        )

    return buffer


if __name__ == "__main__":
    """
       The instruction how to run doctest with the pytest:
    - Install Python 3.8 (https://www.python.org/downloads/)
    - Install pytest `pip install pytest`
    - Clone the repository <path your repository>
    - Checkout branch <your branch>
    - Open terminal
    - Write the following comand: pytest --doctest-modules
    """
    import doctest

    doctest.testmod()
