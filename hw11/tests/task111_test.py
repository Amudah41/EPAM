import pytest
from hw11.tasks.task111 import SimplifiedEnum


def test_working_with_one_class():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"


def test_working_with_two_classes():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert ColorsEnum.BLACK == "BLACK" and SizesEnum.XL == "XL"
