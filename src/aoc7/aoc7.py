from src.aoc7.camel_card_game import CamelCardGame
from src.utils.input.puzzle_input_file import PuzzleInputFile

if __name__ == '__main__':
    puzzle_file = PuzzleInputFile(7, 1, '#', " ")
    card_game = CamelCardGame(puzzle_file.puzzle_input_lines)

    print(f"The total winnings are = {card_game.total_winnings} \n\n")
