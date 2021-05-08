"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""


from contextlib import contextmanager
import sys


class supressor_class:
    def __init__(self, err: BaseException):
        self.err = err

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.err:
            sys.excepthook = lambda x, y, z: ...


@contextmanager
def supressor_generator(err: BaseException):
    try:
        yield
    except err:
        pass
    finally:
        pass


if __name__ == "__main__":
    ...
