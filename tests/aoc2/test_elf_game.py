import pytest
from aoc2.cube_container import CubeContainer
from aoc2.elf_game import ElfGame


class TestElfGame:

    @pytest.mark.parametrize("input_game, expected_value",
                             [(ElfGame(1, [CubeContainer(12, 0, 3), CubeContainer(4, 13, 3), CubeContainer(4, 0, 14)]),
                               True),
                              (ElfGame(2, [CubeContainer(20, 13, 14), CubeContainer(12, 20, 14),
                                           CubeContainer(12, 13, 20)]),
                               False)])
    def test_possible_game(self, input_game, aoc2_bag, expected_value):
        assert input_game.possible_game(aoc2_bag) == expected_value
