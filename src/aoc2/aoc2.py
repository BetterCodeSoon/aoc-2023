import src.utils.file_helper as file_helper
from aoc2.bag import Bag
from aoc2.elf_game import ElfGame


def evaluate_game(elf_game: ElfGame, bag: Bag) -> bool:
    return elf_game.possible_game(bag)


if __name__ == '__main__':
    puzzle_path = file_helper.puzzle_input_path(2, 1)
    file_lines = file_helper.read_file_lines(puzzle_path)

    # toDo Puzzle Solution
