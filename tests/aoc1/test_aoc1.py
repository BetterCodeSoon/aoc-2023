import pytest
import src.aoc1.aoc1 as aoc1
import src.utils.file_helper as file_helper


def puzzle1_tuple_list():
    file_path = file_helper.puzzle_testcases_path(1, 1)
    return file_helper.read_test_values_tuple_list(file_path, ":")


def replace_digits_testcases():
    file_path = file_helper.puzzle_testcases_path(1, 2)
    return file_helper.read_test_values_tuple_list(file_path, ":")


def find_values_testcases():
    file_path = file_helper.puzzle_testcases_path(1, 3)
    return file_helper.read_test_values_tuple_list(file_path, ":")


class TestAoc1:

    @pytest.mark.parametrize("input_str, expected_value", puzzle1_tuple_list())
    def test_find_calibration_value(self, input_str, expected_value):
        assert aoc1.find_calibration_value(input_str) == expected_value

    @pytest.mark.parametrize("input_string, expected_value", replace_digits_testcases())
    def test_replace_written_digits(self, input_string, expected_value):
        assert aoc1.replace_written_digits(input_string) == expected_value

    @pytest.mark.parametrize("input_string, expected_value",
                             [("abc123def456", [3, 4, 5, 9, 10, 11])])
    def test_find_digits(self, input_string, expected_value):
        assert aoc1.find_digits(input_string) == expected_value

    @pytest.mark.parametrize("input_string, expected_value",
                             [("two1nine", {'two': [0], 'nine': [4]}),
                              ("11two", {'two': [2]}),
                              ("daksaslasa", {}),
                              ("111", {}),
                              ("7pqrstsixteen", {'six': [6]}), ])
    def test_find_written_digits(self, input_string, expected_value):
        found_digits = aoc1.find_written_digits(input_string)
        assert found_digits == expected_value

    @pytest.mark.parametrize("input_string, start_index, replacement_str, end_index, expected_value",
                             [("testinputbla123", "4", "12345", "9", "test12345bla123"),
                              ("testthreebla123", "4", "3", "9", "test3bla123")])
    def test_replace_str(self, input_string, start_index, replacement_str, end_index, expected_value):
        assert aoc1.replace_str(input_string, int(start_index), replacement_str, int(end_index)) == expected_value

    @pytest.mark.parametrize("input_string, expected_value", find_values_testcases())
    def test_find_values(self, input_string, expected_value):
        assert aoc1.find_values(input_string) == expected_value

    @pytest.mark.parametrize("input_string, expected_value",
                             # [key_with_max_value, highest_index]
                             [({'two': [1, 39], 'nine': [35], 'three': [25]}, ["two", 1])])
    def test_lowest_index_digit(self, input_string, expected_value):
        assert aoc1.lowest_index_digit(input_string) == expected_value

    @pytest.mark.parametrize("input_string, expected_value",
                             # [key_with_max_value, highest_index]
                             [({'five': [1, 39], 'nine': [35], 'three': [25]}, ["five", 39])])
    def test_highest_index_digit(self, input_string, expected_value):
        assert aoc1.highest_index_digit(input_string) == expected_value
