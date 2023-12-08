import pytest
import src.aoc1.aoc1 as aoc1
import src.utils.file_helper as file_helper
import conftest  # this works despite pycharm thinking its unused
from conftest import testfile1_delimiter

# only a commit msg test
def puzzle1_tuple_list():
    file_path = file_helper.puzzle_testcases_path(1, 1)
    return file_helper.read_test_values_tuple_list(file_path, ":")


class TestAoc1:

    @pytest.mark.parametrize("input_str, expected_value", puzzle1_tuple_list())
    def test_cali_value(self, input_str, expected_value):
        assert aoc1.find_calibration_value(input_str) == expected_value

    @pytest.mark.parametrize("input_string, expected_value",
                             [("1abc2", "12"),
                              ("pqr3stu8vwx", "38"),
                              ("a1b2c3d4e5f", "15"),
                              ("dajslasa", "00"),
                              ("treb7uchet", "77"), ])
    def test_multiple_find_calibration_value(self, input_string, expected_value):
        assert aoc1.find_calibration_value(input_string) == expected_value

    @pytest.mark.parametrize("input_string, expected_value",
                             [("seventhree1eightztszfourfivesix", "7three1eightztszfourfive6"),
                              ("five11eight1", "51181"),
                              ("4nineeightseven2", "49eight72"),
                              ("one", "1"),
                              ("xtwo", "x2"),
                              ("three", "3"),
                              ("four", "4"),
                              ("fivexas", "5xas"),
                              ("12six", "126"),
                              ("sevenLDAS", "7LDAS"),
                              ("eight", "8"),
                              ("nine", "9"),
                              ("two1nine", "219"),
                              ("eightwothree", "8wo3"),
                              ("abcone2threexyz", "abc123xyz"),
                              ("xtwone3four", "x2ne34"),
                              ("zoneight234", "z1ight234"),
                              ("7pqrstsixteen", "7pqrst6teen"), ])
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
