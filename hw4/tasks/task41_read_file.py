"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""


import os
import sys
from typing import Callable


def file_producer(text: str):
    with open("temporary.txt", "w") as f:
        f.write(text)

    def my_wrapper(func: Callable):
        output = func("temporary.txt")
        f.close()
        os.remove("temporary.txt")
        return output

    return my_wrapper


def read_magic_number_only_value_error(path: str) -> bool:
    try:
        with open(path, "r") as fi:
            return is_useful_number(float(fi.readline().strip()))
    except:
        raise ValueError("Somthing came wrong.")


def is_useful_number(number: float) -> bool:
    return 1 <= number < 3


if __name__ == "__main__":
    ...
