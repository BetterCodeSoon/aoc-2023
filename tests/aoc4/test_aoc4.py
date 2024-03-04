import src.aoc4.aoc4 as aoc4
from src.utils.input.puzzle_input_file import PuzzleInputFile


class TestAoc4:

    def test_aoc4_solution(self):
        expected_total_points = 17782
        puzzle_file = PuzzleInputFile(4, 1, "#", ":")
        cards = aoc4.cards(puzzle_file)
        total_points = aoc4.total_points(cards)
        assert total_points == expected_total_points
