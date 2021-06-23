import pytest
from hw11.tasks.task112 import Order


def test_working_with_one_function():
    def morning_discount(order):
        return order.price * 0.5

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50


def test_working_with_two_functions():
    def morning_discount(order):
        return order.price - order.price * 0.5

    def elder_discount(order):
        return order.price - order.price * 0.9

    order_1 = Order(100, morning_discount)
    order_2 = Order(100, elder_discount)

    assert order_1.final_price() == 50 and order_2.final_price() == 10
