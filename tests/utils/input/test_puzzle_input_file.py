import pytest

from utils.input.input_line import InputLine
from utils.input.puzzle_input_file import PuzzleInputFile


def expected_puzzle_input_lines():
    # expected content for day0_puzzle1_input.txt
    return [InputLine(".........874.772...........787..........556"),
            InputLine(".......*..*.......314............308.......")]


class TestPuzzleInputFile:

    @pytest.mark.parametrize("day, file_number, comment_marker",
                             [(0, 1, '#')])
    def test_input_file_initialization(self, day, file_number, comment_marker):
        input_file = PuzzleInputFile(0, 1, comment_marker)
        assert input_file.puzzle_input_lines == expected_puzzle_input_lines()

    @pytest.mark.parametrize("input_file1, input_file2, expected",
                             [(PuzzleInputFile(0, 1), PuzzleInputFile(0, 1), True),
                              (PuzzleInputFile(0, 1), PuzzleInputFile(0, 2), False)])
    def test_equality(self, input_file1, input_file2, expected):
        assert (input_file1 == input_file2) is expected

    @pytest.mark.parametrize("input_file1, input_file2, expected",
                             [(PuzzleInputFile(0, 1), PuzzleInputFile(0, 1), False),
                              (PuzzleInputFile(0, 1), PuzzleInputFile(0, 2), True)])
    def test_inequality(self, input_file1, input_file2, expected):
        assert (input_file1 != input_file2) is expected
