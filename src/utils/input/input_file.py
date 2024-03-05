from pathlib import Path

from src import VALID_TYPES, TYPE_TESTCASE, TYPE_PUZZLE
from src.utils import file_helper


class InputFile:

    def __init__(self, file_type: str, day: int, file_number: int, comment_marker: str = '#', rstrip: bool = True):

        if file_type is None:
            raise Exception(f"Ahhh panic!!! The file type is None! x_x")

        if file_type not in VALID_TYPES:
            raise ValueError(f"The file type: {file_type} is not a valid type")

        self.file_path: Path = self._get_path(file_type, day, file_number)
        self.file_lines: [str] = file_helper.read_file_lines(self.file_path, comment_marker, rstrip)

    @staticmethod
    def _get_path(file_type: str, day: int, file_number: int):
        if file_type is TYPE_PUZZLE:
            return file_helper.puzzle_input_path(day, file_number)
        elif file_type is TYPE_TESTCASE:
            return file_helper.puzzle_testcases_path(day, file_number)
        else:
            raise Exception(f"Cannot create path for file type: {file_type}")

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return self.file_path == other.file_path and self.file_lines == other.file_lines

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.file_path, tuple(self.file_lines)))
