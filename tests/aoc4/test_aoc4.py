from src.aoc4.aoc4 import cards, total_points
from src.aoc4.scratchcards import Scratchcards
from src.utils.input.puzzle_input_file import PuzzleInputFile


class TestAoc4:

    def test_aoc4_solution(self):
        expected_total_points = 17782
        expected_total_cards = 8477787
        puzzle_file = PuzzleInputFile(4, 1, "#", ":")
        cards_list = cards(puzzle_file)
        assert total_points(cards_list) == expected_total_points
        assert Scratchcards(cards_list).total_cards == expected_total_cards
