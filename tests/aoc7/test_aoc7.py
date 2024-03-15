from src.aoc7.camel_card_game import CamelCardGame
from src.utils.input.puzzle_input_file import PuzzleInputFile


class TestAoc7:

    def test_aoc7(self):
        puzzle_file = PuzzleInputFile(7, 1, '#', " ")
        card_game = CamelCardGame(puzzle_file.puzzle_input_lines)
        # Part 1:
        assert card_game.total_winnings == 248105065
