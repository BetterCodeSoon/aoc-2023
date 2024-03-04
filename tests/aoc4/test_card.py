import pytest

from src.aoc4.card import Card
from src.utils.input.input_line import InputLine
from src.utils.input.testcase_input_file import TestcaseInputFile


def testcase_input_file(day, number, comment_marker: str = '#', values_delimiter: str = '|',
                        value_separator: str = ',') -> TestcaseInputFile:
    return TestcaseInputFile(day, number, comment_marker, values_delimiter, value_separator)


def flat_int_list(value_list: [[str]]) -> [int]:
    return [int(value) for sublist in value_list for value in sublist if value != '']


class TestCard:
    day: int = 4
    comment_marker: str = '#'
    values_delimiter: str = ':'
    value_separator: str = '='

    testcase_1_file = testcase_input_file(day, 1, comment_marker, values_delimiter, value_separator)

    testcase_1_input_lines: [InputLine] = testcase_1_file.testcase_input_lines
    testcase_1_expected_values: [[str]] = testcase_1_file.testcase_expected_values

    @pytest.mark.parametrize("input_str, expected_winning_num, expected_card_nums, expected_matches, expected_points", [
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53], 4, 8)
    ])
    def test_initialization(self, input_str, expected_winning_num, expected_card_nums, expected_matches,
                            expected_points):
        card = Card(InputLine(input_str, ":", True))

        assert card.game_id == 1
        assert card.winning_numbers == expected_winning_num
        assert card.card_numbers == expected_card_nums
        assert card.matches == expected_matches
        assert card.points == expected_points
