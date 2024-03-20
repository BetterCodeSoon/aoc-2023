from src.aoc7.camel_card_game import CamelCardGame
from src.utils.input.puzzle_input_file import PuzzleInputFile


class TestAoc7:

    def test_aoc7(self):
        puzzle_file = PuzzleInputFile(7, 1, '#', " ")

        # Part 1:
        card_game = CamelCardGame(puzzle_file.puzzle_input_lines)
        assert card_game.total_winnings == 248105065

        # Part 2:
        joker_card_game = CamelCardGame(puzzle_file.puzzle_input_lines, True)
        assert joker_card_game.total_winnings == 249515436
