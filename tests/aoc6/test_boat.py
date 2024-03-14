import pytest

from src.aoc6.boat import Boat


class TestBoat:

    @pytest.mark.parametrize("time_button_pressed, max_race_duration, expected", [
        (1, 7, 6),
        (2, 7, 10),
        (3, 7, 12)
    ])
    def test_calc_distance(self, time_button_pressed, max_race_duration, expected):
        assert Boat.calc_distance(time_button_pressed, max_race_duration) == expected
