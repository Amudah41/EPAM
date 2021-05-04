"""
Homework 2:
============

Preamble
========

We have a database file (example.sqlite) in sqlite3 format with some tables and data. All tables have 'name' column and maybe some additional ones.

Data retrieval and modifications are done with sqlite3 module by issuing SQL statements.
For example, to get all data from TABLE1::

    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from TABLE1')
    data = cursor.fetchall()   # will be a list with data.

instead of getting all data at once, you can use .fetchone() calls and named expressions::

    while row:=cursor.fetchone():
        print(row)

To get a row with specific
 name equal to some value::

    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from presidents where name=:name', {name:'Yeltsin'})
    data = cursor.fetchall()  # will get all records with this name. You can also use .fetchone() to get one record.

in order to get record with first name (sorted alphabetically) use SQL expression `SELECT * from presidents order by name asc limit 1`
in order to get record after specified (sorted alphabetically) use SQL expression `SELECT * from presidents where name > :name order by name limit`.
To get amount of records in table TABLE1, use `select count(*) from TABLE1` query.


Please refer to this documents for more information about how to retrieve data from sqlite database:
DBAPI: https://www.python.org/dev/peps/pep-0249/
sqlite3 module: https://docs.python.org/3/library/sqlite3.html


Task
====

Write a wrapper class TableData for database table, that when initialized with database name and table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
 -  `len(presidents)` will give current amount of rows in presidents table in database
 -  `presidents['Yeltsin']` should return single data row for president with name Yeltsin
 -  `'Yeltsin' in presidents` should return if president with same name exists in table
 -  object implements iteration protocol. i.e. you could use it in for loops::
       for president in presidents:
           print(president['name'])
 - all above mentioned calls should reflect most recent data. If data in table changed after you created collection instance, your calls should return updated data.

Avoid reading entire table into memory. When iterating through records, start reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls completely. Use supplied example.sqlite file as database fixture file.

"""
import sqlite3
from typing import Tuple, Any, List, Dict


class TableData:
    def __init__(self, database_name: str = "", table_name: str = "") -> None:
        self.conn = sqlite3.connect(database_name)
        self.table_name = table_name

    def __len__(self) -> int:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        return cursor.fetchone()[0]

    def __contains__(self, item_name: str) -> bool:
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT * FROM {self.table_name} where name=:name", {"name": item_name}
        )
        return bool(cursor.fetchall())

    def __getitem__(self, item_name: str) -> Tuple[Any]:
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT * FROM {self.table_name} where name=:name", {"name": item_name}
        )
        return cursor.fetchone()

    def __iter__(self) -> "TableData":
        self.number_of_row = 0
        self.colomns = self.name_of_table_colomns()
        print(type(self))
        return self

    def name_of_table_colomns(self) -> List[str]:
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT name FROM PRAGMA_TABLE_INFO(:table)", {"table": self.table_name}
        )
        return [colomn[0] for colomn in cursor.fetchall()]

    def __next__(self) -> Dict[str, Any]:
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT * from presidents limit {self.number_of_row}, {self.number_of_row +1}"
        )
        next_row = cursor.fetchone()
        if not next_row:
            raise StopIteration
        self.number_of_row += 1
        return dict(zip(self.colomns, next_row))


if __name__ == "__main__":
    ...
