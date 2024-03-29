import pytest

import src.utils.file_helper as file_helper
from src.aoc2 import aoc2_input_helper
from src.aoc2.elf_game import ElfGame
from src.aoc2.cube_container import CubeContainer


def max_color_testcases_dict():
    file_path = file_helper.puzzle_testcases_path(2, 2)
    game_min_values_tuple_list = file_helper.read_test_values_tuple_list(file_path, "#")

    elf_game_max_red_list = []
    elf_game_max_green_list = []
    elf_game_max_blue_list = []

    for elf_game_str, min_values in game_min_values_tuple_list:
        max_values_list = min_values.split(".")
        elf_game = aoc2_input_helper.str_to_elf_game(str(elf_game_str))
        elf_game_max_red_list.append((elf_game, int(max_values_list[0])))
        elf_game_max_green_list.append((elf_game, int(max_values_list[1])))
        elf_game_max_blue_list.append((elf_game, int(max_values_list[2])))

    # need --> [(ElfGame, int)] for R,G,B respectively
    return {'R': elf_game_max_red_list, 'G': elf_game_max_green_list, 'B': elf_game_max_blue_list}


def elf_game_expected_max_color_list(color_testcases_dict, key):
    return color_testcases_dict[key]


def read_example_testcases() -> [(ElfGame, bool)]:
    """
    e.g. for input: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green#1" \n\n
    return  [(ElfGame(1, [CubeContainer(4, 0, 3), CubeContainer(1, 2, 6), CubeContainer(0, 2, 6)], True)]  \n
    """
    file_path = file_helper.puzzle_testcases_path(2, 1)
    game_tuple_list = file_helper.read_test_values_tuple_list(file_path, ":")

    elf_game_eval_list = []

    for input_tuple in game_tuple_list:

        game_id = aoc2_input_helper.read_game_id(input_tuple[0])
        game_sets_str, correct_evaluation = input_tuple[1].split("#")
        game_sets = aoc2_input_helper.read_game_sets_list(game_sets_str)
        elf_game_eval_list.append((ElfGame(game_id, game_sets), bool(int(correct_evaluation))))

    return elf_game_eval_list


class TestElfGame:

    @pytest.mark.parametrize("input_game, expected", read_example_testcases())
    def test_possible_game(self, input_game, aoc2_bag, expected):
        assert input_game.possible_game(aoc2_bag) == expected

    @pytest.mark.parametrize("elf_game1, elf_game2, expected",
                             [(aoc2_input_helper.str_to_elf_game(
                                 "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
                               aoc2_input_helper.str_to_elf_game(
                                   "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
                               True),
                              (aoc2_input_helper.str_to_elf_game(
                                  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
                               aoc2_input_helper.str_to_elf_game(
                                   "Game 1: 3 blue, 1 red; 1 red, 2 green, 444 blue; 2 green"),
                               False)])
    def test_equality_operator(self, elf_game1, elf_game2, expected):
        assert (elf_game1 == elf_game2) == expected

    @pytest.mark.parametrize("elf_game1, elf_game2, expected",
                             [(aoc2_input_helper.str_to_elf_game(
                                 "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
                               aoc2_input_helper.str_to_elf_game(
                                   "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
                               False),
                              (aoc2_input_helper.str_to_elf_game(
                                  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
                               aoc2_input_helper.str_to_elf_game(
                                   "Game 1: 3 blue, 1 red; 1 red, 2 green, 444 blue; 2 green"),
                               True)])
    def test_inequality_operator(self, elf_game1, elf_game2, expected):
        assert (elf_game1 != elf_game2) == expected

    @pytest.mark.parametrize("input_elf_game, expected",
                             elf_game_expected_max_color_list(max_color_testcases_dict(), 'R'))
    def test_max_red_value(self, input_elf_game, expected):
        assert input_elf_game.max_red_value() == expected

    @pytest.mark.parametrize("input_elf_game, expected",
                             elf_game_expected_max_color_list(max_color_testcases_dict(), 'G'))
    def test_max_green_value(self, input_elf_game, expected):
        assert input_elf_game.max_green_value() == expected

    @pytest.mark.parametrize("input_elf_game, expected",
                             elf_game_expected_max_color_list(max_color_testcases_dict(), 'B'))
    def test_max_blue_value(self, input_elf_game, expected):
        assert input_elf_game.max_blue_value() == expected

    @pytest.mark.parametrize("input_elf_game, expected",
                             [(aoc2_input_helper.str_to_elf_game(
                                 "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
                               48),
                              (aoc2_input_helper.str_to_elf_game(
                                  "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"),
                               1560)])
    def test_calc_power(self, input_elf_game, expected):
        assert input_elf_game.calc_power() == expected
