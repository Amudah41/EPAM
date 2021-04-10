import pytest

from hw4.tasks.task43_get_print_output import my_precious_logger


@pytest.mark.parametrize(
    ["message", "expected_result"],
    [["error: file not found", "'error: file not found'\n"]],
)
def test_my_precious_logger_err(capsys, message: int, expected_result: str):
    my_precious_logger(message)
    captured = capsys.readouterr()
    assert captured.err == expected_result


@pytest.mark.parametrize(
    ["message", "expected_result"], [["OK", "'OK'\n"], ["", "''\n"]]
)
def test_my_precious_logger_out(capsys, message: int, expected_result: str):
    my_precious_logger(message)
    captured = capsys.readouterr()
    assert captured.out == expected_result
