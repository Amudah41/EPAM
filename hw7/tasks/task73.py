"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished!"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    n = len(board[0])

    if ["x"] * n in board:
        return "x wins!"
    if ["o"] * n in board:
        return "o wins!"

    flat_board = [char for row in board for char in row]
    for i in range(n):
        if (
            all(flat_board[j] == flat_board[i] for j in range(n + i, n * n, n))
            and flat_board[i] != "-"
        ):  # search in colomns
            return f"{flat_board[i]} wins!"
    if (
        all(flat_board[j] == flat_board[0] for j in range(n + 1, n * n, n + 1))
        and flat_board[0] != "-"
    ):  # search in the main diagonal
        return f"{flat_board[0]} wins!"
    if (
        all(
            flat_board[j] == flat_board[n - 1]
            for j in range(n - 1, n * (n - 1) + 1, n - 1)
        )
        and flat_board[n - 1] != "-"
    ):  # search in the side diagonal
        return f"{flat_board[n-1]} wins!"
    if "-" in flat_board:
        return "unfinished!"
    return "draw!"


if __name__ == "__main__":
    ...
