from src.aoc4.card import Card
from src.aoc4.scratchcards import Scratchcards
from src.utils.input.puzzle_input_file import PuzzleInputFile


def cards(puzzle_input_file: PuzzleInputFile):
    return [Card(input_line) for input_line in puzzle_input_file.puzzle_input_lines]


def total_points(cards_list: [Card]):
    return sum(card.points for card in cards_list)


if __name__ == '__main__':
    puzzle_file = PuzzleInputFile(4, 1, "#", ":")
    cards_list = cards(puzzle_file)
    print(f"The total points of all the cards = {total_points(cards_list)} \n")
    print(f"The total number of scratchcards = {Scratchcards(cards_list).total_cards} \n")
