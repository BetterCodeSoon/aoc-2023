import pytest
import src.aoc2.aoc2 as aoc2
import src.utils.file_helper as file_helper
from aoc2 import input_helper
from aoc2.elf_game import ElfGame


def read_example_testcases() -> [(ElfGame, bool)]:
    """
    e.g. for input: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green#1" \n\n
    return  [(ElfGame(1, [CubeContainer(4, 0, 3), CubeContainer(1, 2, 6), CubeContainer(0, 2, 6)], True)]  \n
    """
    file_path = file_helper.puzzle_testcases_path(2, 1)
    game_tuple_list = file_helper.read_test_values_tuple_list(file_path, ":")

    elf_game_eval_list = []

    for input_tuple in game_tuple_list:
        game_id = input_helper.read_game_id(input_tuple[0])
        game_sets_str, correct_evaluation = input_tuple[1].split("#")
        game_sets = input_helper.read_game_sets_list(game_sets_str)

        elf_game_eval_list.append((ElfGame(game_id, game_sets), bool(int(correct_evaluation))))

    return elf_game_eval_list


class TestAoc2:

    @pytest.mark.parametrize("input_game, expected", read_example_testcases())
    def test_example_testcases(self, input_game, aoc2_bag, expected):
        assert aoc2.evaluate_game(input_game, aoc2_bag) == expected
