import src.utils.file_helper as file_helper
import src.aoc2.aoc2_input_helper as input_helper

from src.aoc2.bag import Bag
from src.aoc2.elf_game import ElfGame

if __name__ == '__main__':
    id_sum = 0
    power_sum = 0
    game_bag = Bag(12, 13, 14)
    puzzle_path = file_helper.puzzle_input_path(2, 1)
    file_lines = file_helper.read_file_lines(puzzle_path)

    for line in file_lines:
        game_str, game_sets_str = line.rstrip("\n").split(": ")
        game_id = input_helper.read_game_id(game_str)
        game_sets = input_helper.read_game_sets_list(game_sets_str)

        elf_game = ElfGame(game_id, game_sets)

        if elf_game.possible_game(game_bag):
            id_sum += game_id

        power_sum += elf_game.calc_power()

    print(f"Given the Bag: 12 red cubes, 13 green cubes, 14 blue cubes\n")
    print(f"The sum of the IDs of all possible games = {id_sum}\n")
    print(f"The sum of the power of all games = {power_sum}\n")
