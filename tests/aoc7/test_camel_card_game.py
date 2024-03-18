import pytest

from src.aoc7.camel_card_game import CamelCardGame
from src.utils.input.testcase_input_file import TestcaseInputFile


class TestCamelCardGame:
    testcases_file1 = TestcaseInputFile(7, 1, '#', " ", "|")

    @pytest.mark.parametrize("joker_rule, expected_winnings", [
        (True, 5905),
        (False, 6440)
    ])
    def test_initialization(self, joker_rule, expected_winnings):
        card_game = CamelCardGame(self.testcases_file1.testcase_input_lines, joker_rule)
        assert card_game.total_winnings == expected_winnings
