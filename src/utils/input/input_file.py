from pathlib import Path

from src import VALID_TYPES, TYPE_TESTCASE, TYPE_PUZZLE
from src.utils import file_helper
from src.utils.input.input_line import InputLine


class InputFile:
    file_path: Path
    file_lines = [InputLine]

    def __init__(self, file_type: str, day: int, file_number: int, comment_marker: str = '#'):

        if file_type is None:
            raise Exception(f"Ahhh panic!!! The file type is None! x_x")

        if file_type not in VALID_TYPES:
            raise ValueError(f"The file type: {file_type} is not a valid type")

        self.file_path = self._get_path(file_type, day, file_number)
        self.file_lines = file_helper.read_file_lines(self.file_path, comment_marker)

    @staticmethod
    def _get_path(file_type: str, day: int, file_number: int):
        if file_type is TYPE_PUZZLE:
            return file_helper.puzzle_input_path(day, file_number)
        elif file_type is TYPE_TESTCASE:
            return file_helper.puzzle_testcases_path(day, file_number)
        else:
            raise Exception(f"Cannot create path for file type: {file_type}")

    def __eq__(self, other):
        return self.file_path == other.file_path and self.file_lines == other.file_lines

    def __ne__(self, other):
        return not self.__eq__(other)
