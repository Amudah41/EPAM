import pytest
import sqlite3
from hw8.tasks.task82 import TableData


def test_positive_connection():
    TableData(database_name="./hw8/example.sqlite", table_name="presidents")
    assert True


def test_len_of_item():
    presidents = TableData(
        database_name="./hw8/example.sqlite", table_name="presidents"
    )
    assert len(presidents) == 3


def test_get_item():
    presidents = TableData(
        database_name="./hw8/example.sqlite", table_name="presidents"
    )
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_item_name_in_table():
    presidents = TableData(
        database_name="./hw8/example.sqlite", table_name="presidents"
    )
    assert "Yeltsin" in presidents


def test_item_name_not_in_table():
    presidents = TableData(
        database_name="./hw8/example.sqlite", table_name="presidents"
    )
    assert not "Putin" in presidents


def test_table_as_iterator():
    presidents = TableData(
        database_name="./hw8/example.sqlite", table_name="presidents"
    )
    actual_result = []
    for president in presidents:
        actual_result.append(president["name"])

    assert actual_result == ["Yeltsin", "Trump", "Big Man Tyrone"]
