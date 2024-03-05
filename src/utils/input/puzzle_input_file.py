from src import TYPE_PUZZLE
from src.utils.input.input_file import InputFile
from src.utils.input.input_line import InputLine


class PuzzleInputFile(InputFile):

    def __init__(self, day: int, file_number: int, comment_marker: str = '#', delimiter: str = "",
                 strip_trailing_whitespaces: bool = True):
        super().__init__(TYPE_PUZZLE, day, file_number, comment_marker)
        self.puzzle_input_lines = [InputLine(line, delimiter, strip_trailing_whitespaces) for line in self.file_lines]

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return super().__eq__(other) and self.puzzle_input_lines == other.puzzle_input_lines

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.file_path, tuple(self.file_lines), tuple(self.puzzle_input_lines)))
