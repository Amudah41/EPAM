"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


>>> my_precious_logger("error: file not found")
'error: file not found'


>>> my_precious_logger("OK")
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout


"""
import sys


def my_precious_logger(text: str):
    if type(text) != str:
        raise ValueError("text must be exact string")
    if text == "":
        sys.stdout.write("''\n")
        return None

    if text.split()[0][:5] == "error":
        sys.stderr.write("'" + text + "'\n")
        # print("# stderr\n" + "'" + text + "'\n")
    else:
        sys.stdout.write("'" + text + "'\n")


if __name__ == "__main__":
    ...
