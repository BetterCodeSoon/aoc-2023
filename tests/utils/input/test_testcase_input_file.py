import pytest

from src.utils.input.input_line import InputLine
from src.utils.input.testcase_input_file import TestcaseInputFile


def expected_testcase_input_lines() -> [InputLine]:
    # expected content for day0_testcases1.txt
    return [InputLine("467..114..| 144", "|"),
            InputLine("...*......", "|"),
            InputLine("..11.+.58.| 11, 58", "|")]


def expected_testcase_values() -> [str]:
    return [['144'], [''], ['11', '58']]


class TestTestcaseInputFile:

    @pytest.mark.parametrize("day, file_number, comment_marker, values_delimiter, value_separator",
                             [(0, 1, '~', "|", ',')])
    def test_input_file_initialization(self, day, file_number, comment_marker, values_delimiter, value_separator):
        input_file = TestcaseInputFile(0, 1, comment_marker, values_delimiter, value_separator)
        assert input_file.testcase_input_lines == expected_testcase_input_lines()
        assert input_file.testcase_expected_values == expected_testcase_values()

    @pytest.mark.parametrize("input_file1, input_file2, expected",
                             [(TestcaseInputFile(0, 1), TestcaseInputFile(0, 1), True),
                              (TestcaseInputFile(0, 1), TestcaseInputFile(0, 2), False)])
    def test_equality(self, input_file1, input_file2, expected):
        assert (input_file1 == input_file2) is expected

    @pytest.mark.parametrize("input_file1, input_file2, expected",
                             [(TestcaseInputFile(0, 1), TestcaseInputFile(0, 1), False),
                              (TestcaseInputFile(0, 1), TestcaseInputFile(0, 2), True)])
    def test_inequality(self, input_file1, input_file2, expected):
        assert (input_file1 != input_file2) is expected
