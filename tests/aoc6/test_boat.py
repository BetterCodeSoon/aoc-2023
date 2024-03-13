import pytest

from src.aoc6.boat import Boat


class TestBoat:

    @pytest.mark.parametrize("time_button_pressed, max_race_duration, expected", [
        (1, 7, 6),
        (2, 7, 10),
        (3, 7, 12)
    ])
    def test_calc_distance(self, time_button_pressed, max_race_duration, expected):
        assert Boat._calc_distance(time_button_pressed, max_race_duration) == expected

    @pytest.mark.parametrize("time_button_pressed, max_race_duration, expected_distance", [
        (1, 7, 6),
        (2, 7, 10),
        (3, 7, 12)
    ])
    def test_hold_button(self, time_button_pressed, max_race_duration, expected_distance):
        boat = Boat(max_race_duration)
        boat.hold_button(time_button_pressed)
        assert boat.speed == time_button_pressed
        assert boat.distance_traveled == expected_distance
