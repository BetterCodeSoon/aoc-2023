from src.aoc7.camel_card_game import CamelCardGame
from src.utils.input.testcase_input_file import TestcaseInputFile


class TestCamelCardGame:
    testcases_file1 = TestcaseInputFile(7, 1, '#', " ", "|")

    def test_initialization(self):
        card_game = CamelCardGame(self.testcases_file1.testcase_input_lines)
        assert card_game.total_winnings == 6440
