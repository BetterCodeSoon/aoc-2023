import pytest
import src.aoc1.aoc1 as aoc1


@pytest.mark.parametrize("input_string, expected_value",
                         [("1abc2", "12"),
                          ("pqr3stu8vwx", "38"),
                          ("a1b2c3d4e5f", "15"),
                          ("dajslasa", "00"),
                          ("treb7uchet", "77"),])
def test_multiple_find_calibration_value(input_string, expected_value):
    assert aoc1.find_calibration_value(input_string) == expected_value


@pytest.mark.parametrize("input_string, expected_value",
                         [("one", "1"),
                          ("xtwo", "x2"),
                          ("three", "3"),
                          ("four", "4"),
                          ("fivexas", "5xas"),
                          ("12six", "126"),
                          ("sevenLDAS", "7LDAS"),
                          ("eight", "8"),
                          ("nine", "9"),])
def test_replace_written_digits(input_string, expected_value):
    assert aoc1.replace_written_digits(input_string) == expected_value
