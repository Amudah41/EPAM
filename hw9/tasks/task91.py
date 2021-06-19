"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator, Tuple, Optional
from contextlib import ExitStack


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname)) for fname in file_list]
        buffer = []
        for index, file in enumerate(files):
            file_is_not_empty, value = value_from_file(file)
            if file_is_not_empty:
                pase(buffer, index, value)

        if buffer == []:
            return StopIteration

        while True:
            output = buffer.pop()
            yield output[1]
            file_is_not_empty, value = value_from_file(files[output[0]])
            if file_is_not_empty:
                pase(buffer, output[0], value)
            elif buffer == []:
                return StopIteration


def value_from_file(file: "_io.TextIOWrapper") -> Tuple[bool, Optional[int]]:
    try:
        value = int(file.readline())
        return True, value
    except ValueError:
        return False, None


def pase(buffer, index, value) -> None:

    if buffer == [] or value <= buffer[-1][1]:
        return buffer.append([index, value])

    if value > buffer[0][1]:
        return buffer.insert(0, [index, value])

    for locat_index, item in enumerate(buffer):
        if item[1] >= value:
            continue
        return buffer.insert(locat_index, [index, value])


if __name__ == "__main__":
    ...
