from utils.input.input_file import InputFile
from src import TYPE_TESTCASE


def read_tcase1_file():
    return InputFile(TYPE_TESTCASE, 5, 1, "#", False)


def tcase1_file_lines():
    return read_tcase1_file().file_lines
