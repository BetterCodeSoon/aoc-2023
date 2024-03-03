import pytest
from aoc2.bag import Bag
from aoc2.cube_container import CubeContainer


class TestBag:
    @pytest.mark.parametrize("input_bag, input_game_set, expected_value",
                             [(Bag(12, 13, 14), CubeContainer(12, 0, 3), True),
                              (Bag(12, 13, 14), CubeContainer(4, 13, 3), True),
                              (Bag(12, 13, 14), CubeContainer(4, 0, 14), True),
                              (Bag(12, 13, 14), CubeContainer(20, 0, 3), False),
                              (Bag(12, 13, 14), CubeContainer(4, 20, 3), False),
                              (Bag(12, 13, 14), CubeContainer(4, 0, 20), False)])
    def test_reveal_cubes_possible(self, input_bag, input_game_set, expected_value):
        assert input_bag.reveal_cubes_possible(input_game_set) == expected_value
