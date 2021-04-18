"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
import unicodedata
from collections import Counter, defaultdict
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="unicode-escape") as fi:
        n = 10
        stack = [""] * n
        tmp = ""
        for line in fi:

            if line == "\n":
                continue

            line = (
                tmp + line
            )  # добавляем перенесённое слово с прошлой строки к началу текущей строки
            tmp = ""
            word = ""
            if (
                line[-1] == "-"
            ):  # проверяем крайнее слово строки на перенос; удаляем его из текущей строки, если проверка успешная
                line.pop()
                i = -2
                while line[i] != " ":  # находим начало слова на текущей строке
                    tmp = line.pop() + tmp
                    i -= 1
            for letter in line:  # составляем слова из символов
                # удаляем пунктуацию
                if unicodedata.category(letter)[0] == "P":
                    continue
                if letter != " ":
                    word += letter
                    continue
                else:
                    # добавляем слово в стек самых длинных
                    if (
                        len(word) == len(set(word))
                        and len(word) > len(stack[-1])
                        and not word in stack
                    ):
                        stack.pop()
                        if len(word) > len(stack[0]):
                            stack.insert(0, word)
                        else:
                            for index in range(n - 2, -1, -1):
                                if len(stack[index]) >= len(word):
                                    stack.insert(index + 1, word)
                                    break

                word = ""
        return stack


def get_rarest_char(file_path: str) -> str:
    with open(file_path, "r", encoding="unicode-escape") as fi:
        symbols = defaultdict(int)
        for line in fi:
            for letter in line:
                symbols[letter] += 1

        return min(symbols.items(), key=lambda x: x[1])[0]


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as fi:
        count = 0
        for line in fi:
            for letter in line:
                if unicodedata.category(letter)[0] == "P":
                    count += 1
        return count


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as fi:
        count = 0
        for line in fi:
            for letter in line:
                if ord(letter) > 127:
                    count += 1
        return count


def get_most_common_non_ascii_char(file_path: str) -> str:

    with open(file_path, "r", encoding="unicode-escape") as fi:
        symbols = defaultdict(int)
        for line in fi:
            for letter in line:
                if not letter.isascii():
                    symbols[letter] += 1
        return max(symbols.items(), key=lambda x: x[1])[0]
