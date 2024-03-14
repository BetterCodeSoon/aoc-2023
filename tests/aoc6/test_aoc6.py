from src.aoc6.boat_race import BoatRace


class TestAoc6:

    def test_aoc6(self):
        expected_part1 = 114400
        max_durations = [35, 93, 73, 66]
        distance_records = [212, 2060, 1201, 1044]
        assert BoatRace.error_margins_for_race(max_durations, distance_records) == expected_part1
