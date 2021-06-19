import pytest

from hw9.tasks.task92 import supressor_class, supressor_generator, Suppressor


def test_valid_error_class():
    with supressor_class(IndexError):
        [][2]

    assert True


def test_not_valid_error_class():
    with pytest.raises(IndexError):
        with supressor_class(KeyError):
            [][2]
    assert True


def test_valid_error_generetor():
    with supressor_generator(IndexError):
        [][2]
    assert True


def test_not_valid_error_generator():
    with pytest.raises(IndexError):
        with supressor_generator(KeyError):
            [][2]
    assert True
