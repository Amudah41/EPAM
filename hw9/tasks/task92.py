"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""


from contextlib import contextmanager


class supressor_class:
    def __init__(self, err: BaseException) -> None:
        self.err = err

    def __enter__(self) -> "supressor_class":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        return issubclass(exc_type, self.err)


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
