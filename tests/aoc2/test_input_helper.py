import pytest
import src.aoc2.aoc2_input_helper as input_helper
from src.aoc2.cube_container import CubeContainer
from src.aoc2.elf_game import ElfGame


class TestInputHelper:

    @pytest.mark.parametrize("input_color_str, expected", [("3 blue", (3, "blue"))])
    def test_read_color(self, input_color_str, expected):
        assert input_helper.read_color(input_color_str, " ") == expected
        assert input_helper.read_color(input_color_str) == expected

    @pytest.mark.parametrize("input_game_set_str, expected", [("3 blue, 1 red, 2 green", CubeContainer(1, 2, 3)),
                                                              ("2 green, 1 red", CubeContainer(1, 2, 0)),
                                                              ("22 green, 33 blue, 11 red", CubeContainer(11, 22, 33))])
    def test_read_game_set(self, input_game_set_str, expected):
        assert input_helper.read_game_set(input_game_set_str) == expected

    @pytest.mark.parametrize("input_string, expected", [
        ("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
         [CubeContainer(4, 0, 3), CubeContainer(1, 2, 6), CubeContainer(0, 2, 0)]),
        ("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
         [CubeContainer(20, 8, 6), CubeContainer(4, 13, 5), CubeContainer(1, 5, 0)])])
    def test_read_game_sets_list(self, input_string, expected):
        assert input_helper.read_game_sets_list(input_string) == expected

    @pytest.mark.parametrize("game_str, expected", [("Game 1", 1), ("Game 124", 124)])
    def test_read_game_id(self, game_str, expected):
        assert input_helper.read_game_id(game_str, " ") == expected

    @pytest.mark.parametrize("game_str, expected",
                             [("Game 1: 3 blue, 4 red; 1 red, 2 green",
                               ElfGame(1, [CubeContainer(4, 0, 3), CubeContainer(1, 2, 0)]))])
    def test_str_to_elf_game(self, game_str, expected):
        assert input_helper.str_to_elf_game(game_str) == expected
