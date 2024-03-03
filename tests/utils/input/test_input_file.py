import pytest

from src import TYPE_TESTCASE, TYPE_PUZZLE
from src.utils import file_helper
from src.utils.input.input_file import InputFile


def expected_file_lines(file_type: str):
    expected_file_lines_dict = {
        TYPE_PUZZLE: [".........874.772...........787..........556", ".......*..*.......314............308......."],
        TYPE_TESTCASE: ["467..114..| 144", "...*......", "..11.+.58.| 11, 58"]}
    return expected_file_lines_dict[file_type]


class TestInputFile:

    @pytest.mark.parametrize("file_type, day, file_number, comment_marker",
                             [(TYPE_PUZZLE, 0, 1, '#'),
                              (TYPE_TESTCASE, 0, 1, '~')])
    def test_input_file_initialization(self, file_type, day, file_number, comment_marker):
        input_file = InputFile(file_type, 0, 1, comment_marker)
        assert input_file.file_lines == expected_file_lines(file_type)

    @pytest.mark.parametrize("file_type, day, file_number, expected",
                             [(TYPE_PUZZLE, 0, 1, file_helper.puzzle_input_path(0, 1)),
                              (TYPE_TESTCASE, 0, 1, file_helper.puzzle_testcases_path(0, 1))])
    def test_get_path(self, file_type, day, file_number, expected):
        assert InputFile._get_path(file_type, day, file_number) == expected

    @pytest.mark.parametrize("input_file1, input_file2, expected",
                             [(InputFile(TYPE_TESTCASE, 0, 1), InputFile(TYPE_TESTCASE, 0, 1), True),
                              (InputFile(TYPE_PUZZLE, 0, 1), InputFile(TYPE_TESTCASE, 0, 1), False)])
    def test_equality(self, input_file1, input_file2, expected):
        assert (input_file1 == input_file2) is expected

    @pytest.mark.parametrize("input_file1, input_file2, expected",
                             [(InputFile(TYPE_TESTCASE, 0, 1), InputFile(TYPE_TESTCASE, 0, 1), False),
                              (InputFile(TYPE_PUZZLE, 0, 1), InputFile(TYPE_TESTCASE, 0, 1), True)])
    def test_inequality(self, input_file1, input_file2, expected):
        assert (input_file1 != input_file2) is expected

    def test_hash(self):
        day = 0
        number = 1
        file_lines = expected_file_lines(TYPE_TESTCASE)
        file_path = InputFile._get_path(TYPE_TESTCASE, day, number)
        input_file = InputFile(TYPE_TESTCASE, 0, 1, "~")

        assert input_file.__hash__() == hash((file_path, tuple(file_lines)))
