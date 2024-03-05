from aoc4.card import Card
from src.aoc4.scratchcards import Scratchcards
from tests.aoc4.test_card import tcase2_inputs


def testcases2_cards_list() -> [Card]:
    input_lines = [item[0] for item in tcase2_inputs()]
    return [Card(input_line) for input_line in input_lines]


class TestScratchcards:

    def test_initialization(self):
        scratchcards = Scratchcards(testcases2_cards_list())
        assert scratchcards.total_cards == 30
