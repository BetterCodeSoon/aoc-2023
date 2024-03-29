import pytest

from src.aoc6.boat_race import BoatRace


class TestBoatRace:

    @pytest.mark.parametrize("max_race_duration, distance_record, expected_list", [
        (7, 9, [2, 3, 4, 5])
    ])
    def test_ways_to_beat_distance_record(self, max_race_duration: int, distance_record: int, expected_list):
        assert BoatRace._ways_to_beat_distance_record(max_race_duration, distance_record) == expected_list

    @pytest.mark.parametrize("max_race_durations, distance_records, expected", [
        ([7, 15, 30], [9, 40, 200], 288)
    ])
    def test_error_margins_for_race(self, max_race_durations: [int], distance_records: [int], expected):
        assert BoatRace.error_margins_for_race(max_race_durations, distance_records) == expected

    @pytest.mark.parametrize("max_race_durations, distance_records, expected", [
        (7, 9, 2),
        (71530, 940200, 14)
    ])
    def test_find_minimum_way(self, max_race_durations, distance_records, expected):
        assert BoatRace.find_minimum_way(max_race_durations, distance_records) == expected

    @pytest.mark.parametrize("max_race_durations, distance_records, expected", [
        (7, 9, 5),
        (71530, 940200, 71516)
    ])
    def test_find_maximum_way(self, max_race_durations, distance_records, expected):
        assert BoatRace.find_maximum_way(max_race_durations, distance_records) == expected

    @pytest.mark.parametrize("max_race_durations, distance_records, expected", [
        (7, 9, 4),
        (71530, 940200, 71503)
    ])
    def test_ways_by_min_max(self, max_race_durations, distance_records, expected):
        assert BoatRace.ways_by_min_max(max_race_durations, distance_records) == expected
