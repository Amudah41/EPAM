"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable
from sys import path


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    count = 0
    for x in dir_path.iterdir():
        if x.match(f"*.{file_extension}"):
            count += count_from_file(x, tokenizer)
    return count


def count_from_file(file: str, tokenizer: Optional[Callable] = None) -> int:
    with open(file) as fi:
        local_count = 0
        if tokenizer is None:
            for line in fi:
                local_count += 1
        else:
            for line in fi:
                local_count += len(tokenizer(line))
    return local_count


if __name__ == "__main__":
    ...
