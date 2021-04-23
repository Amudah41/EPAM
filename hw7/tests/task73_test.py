import pytest

from hw7.tasks.task73 import tic_tac_toe_checker


def test_tic_tac_toe_checker_x_wins_in_row():
    assert (
        tic_tac_toe_checker([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]])
        == "x wins!"
    )


def test_tic_tac_toe_checker_x_wins_in_colom():
    assert (
        tic_tac_toe_checker([["o", "o", "x"], ["-", "o", "x"], ["o", "x", "x"]])
        == "x wins!"
    )


def test_tic_tac_toe_checker_o_wins_in_main_diag():
    assert (
        tic_tac_toe_checker([["o", "x", "o"], ["-", "o", "x"], ["o", "x", "x"]])
        == "o wins!"
    )


def test_tic_tac_toe_checker_o_wins_in_side_diag():
    assert (
        tic_tac_toe_checker([["o", "x", "o"], ["-", "o", "x"], ["o", "x", "o"]])
        == "o wins!"
    )


def test_tic_tac_toe_checker_draw():
    assert (
        tic_tac_toe_checker([["o", "x", "x"], ["x", "o", "o"], ["o", "o", "x"]])
        == "draw!"
    )


def test_tic_tac_toe_checker_unfinished():
    assert (
        tic_tac_toe_checker([["o", "x", "x"], ["x", "-", "o"], ["o", "o", "x"]])
        == "unfinished!"
    )
