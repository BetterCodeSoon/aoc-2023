import pytest
import src.aoc1.aoc1 as aoc1
import src.utils.file_helper as file_helper
import conftest  # this works despite pycharm thinking its unused
from conftest import testfile1_delimiter


def puzzle1_tuple_list():
    file_path = file_helper.puzzle_testcases_path(1, 1)
    return file_helper.read_test_values_tuple_list(file_path, ":")


def replace_digits_testcases():
    file_path = file_helper.puzzle_testcases_path(1, 2)
    return file_helper.read_test_values_tuple_list(file_path, ":")


class TestAoc1:

    @pytest.mark.parametrize("input_str, expected_value", puzzle1_tuple_list())
    def test_find_calibration_value(self, input_str, expected_value):
        assert aoc1.find_calibration_value(input_str) == expected_value

    @pytest.mark.parametrize("input_string, expected_value", replace_digits_testcases())
    def test_replace_written_digits(self, input_string, expected_value):
        assert aoc1.replace_written_digits(input_string) == expected_value

    @pytest.mark.parametrize("input_string, expected_value",
                             [("two1nine", {'two': 0, 'nine': 4}),
                              ("11two", {'two': 2}),
                              ("daksaslasa", {}),
                              ("111", {}),
                              ("7pqrstsixteen", {'six': 6}), ])
    def test_find_written_digits(self, input_string, expected_value):
        found_digits = aoc1.find_written_digits(input_string)
        assert found_digits == expected_value
