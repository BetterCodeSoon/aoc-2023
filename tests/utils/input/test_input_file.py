import pytest

from src import TYPE_TESTCASE, TYPE_PUZZLE
from src.utils import file_helper
from src.utils.input.input_file import InputFile


class TestInputFile:

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
