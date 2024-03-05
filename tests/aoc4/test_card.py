import pytest

from src.aoc4.card import Card
from src.utils.input.input_line import InputLine
from src.utils.input.testcase_input_file import TestcaseInputFile
from src.utils.string_helper import remove_empty_strings, to_int

DAY: int = 4
COMMENT_MARKER: str = '#'


def testcase_input_file(day, number, comment_marker: str = '#', values_delimiter: str = '|',
                        value_separator: str = ',') -> TestcaseInputFile:
    return TestcaseInputFile(day, number, comment_marker, values_delimiter, value_separator)


def testcase2_inputs():
    testcases2 = testcase_input_file(DAY, 2, COMMENT_MARKER, "=", "value_separator")

    matches_copies_list = [input_line.split(", ") for input_line in testcases2.next_line_parts]
    matches = []
    copies = []

    for match_copies in matches_copies_list:
        matches.append(match_copies[0].lstrip())
        copies.append(match_copies[1].lstrip())

    card_id_winning_num_card_nums = [input_line.line_str.split(":") for input_line in testcases2.testcase_input_lines]
    card_ids = []
    winning_nums = []
    card_nums = []

    for entry in card_id_winning_num_card_nums:
        card_ids.append(Card._remove_non_digits(entry[0]))
        winning_nums.append(remove_empty_strings(entry[1].split(" | ")[0].split(" ")))
        card_nums.append(remove_empty_strings(entry[1].split(" | ")[1].split(" ")))

    input_lines = [InputLine(input_line.line_str, ":") for input_line in testcases2.testcase_input_lines]

    return [(il, int(ci), to_int(wn), to_int(cn), int(m), int(c)) for il, ci, wn, cn, m, c in
            zip(input_lines, card_ids, winning_nums, card_nums, matches, copies)]


class TestCard:

    @pytest.mark.parametrize("input_line, card_id, winning_nums, card_nums, matches, copies", testcase2_inputs())
    def test_initialization(self, input_line, card_id, winning_nums, card_nums, matches, copies):
        card = Card(input_line)

        assert card.card_id == card_id
        assert card.winning_numbers == winning_nums
        assert card.card_numbers == card_nums
        assert card.matches_count == matches
