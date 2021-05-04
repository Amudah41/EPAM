"""
Homework 1:
============


We have a file that works as key-value storage, each like is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song=shadilay
power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name']  # will be string 'kek'
storage.song  # will be 'shadilay'
storage.power  # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when there's a line `1=something`) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
from keyword import iskeyword
from typing import Iterable


class KeyValueStorage:
    def __init__(self, path: str) -> None:
        with open(path) as input:
            self.items = {key: value for key, value in self.splited_lines(input)}

    @staticmethod
    def splited_lines(input: Iterable):
        for line in input:
            line = line.replace("\n", "").split("=")
            if not line[0].isidentifier() or iskeyword(line[0]):
                raise ValueError("Value cannot be assigned to an attribute.")
            yield line[0], line[1]

    def __getitem__(self, key):
        try:
            return int(self.items[key])
        except:
            return self.items[key]

    def __getattr__(self, name):
        try:
            return int(self.items[name])
        except:
            return self.items[name]


if __name__ == "__main__":
    ...
