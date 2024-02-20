import pytest

from src.aoc2.cube_container import CubeContainer


class TestCubeContainer:

    @pytest.mark.parametrize("input_cube1, input_cube2, expected",
                             [(CubeContainer(1, 1, 1), CubeContainer(1, 1, 1), True),
                              (CubeContainer(1, 1, 1), CubeContainer(2, 2, 2), False)])
    def test_equals_operator(self, input_cube1, input_cube2, expected):
        assert (input_cube1 == input_cube2) == expected

    @pytest.mark.parametrize("input_cube1, input_cube2, expected",
                             [(CubeContainer(1, 1, 1), CubeContainer(1, 1, 1), False),
                              (CubeContainer(1, 1, 1), CubeContainer(2, 2, 2), True)])
    def test_inequality_operator(self, input_cube1, input_cube2, expected):
        assert (input_cube1 != input_cube2) == expected
