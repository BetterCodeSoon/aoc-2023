import pytest

from src.aoc3.coordinates import Coordinates


class TestCoordinates:

    @pytest.mark.parametrize("coord1, coord2, expected", [(Coordinates(1, 1), Coordinates(1, 1), True),
                                                          (Coordinates(1, 1), Coordinates(2, 2), False)])
    def test_equality(self, coord1, coord2, expected):
        assert (coord1 == coord2) == expected

    @pytest.mark.parametrize("coord1, coord2, expected", [(Coordinates(1, 1), Coordinates(1, 1), False),
                                                          (Coordinates(1, 1), Coordinates(2, 2), True)])
    def test_inequality(self, coord1, coord2, expected):
        assert (coord1 != coord2) == expected
