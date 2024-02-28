import pytest

from src.aoc3.coordinates_2d import Coordinates2d


class TestCoordinates:

    @pytest.mark.parametrize("coord1, coord2, expected", [(Coordinates2d(1, 1, ), Coordinates2d(1, 1), True),
                                                          (Coordinates2d(1, 1, ), Coordinates2d(2, 2), False)])
    def test_equality(self, coord1, coord2, expected):
        assert (coord1 == coord2) == expected

    @pytest.mark.parametrize("coord1, coord2, expected", [(Coordinates2d(1, 1), Coordinates2d(1, 1), False),
                                                          (Coordinates2d(1, 1), Coordinates2d(2, 2), True)])
    def test_inequality(self, coord1, coord2, expected):
        assert (coord1 != coord2) == expected
