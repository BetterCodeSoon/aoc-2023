import math

from src.aoc6.boat import Boat


class BoatRace:

    @staticmethod
    def _ways_to_beat_distance_record(max_race_duration: int, distance_record: int) -> [int]:
        ways_to_beat_record: [int] = []

        for time_button_pressed in range(0, distance_record):
            distanced_travelled = Boat.calc_distance(time_button_pressed, max_race_duration)
            if distanced_travelled > distance_record:
                ways_to_beat_record.append(time_button_pressed)

        return ways_to_beat_record

    @staticmethod
    def error_margins_for_race(max_race_durations: [int], distance_records: [int]) -> int:
        all_error_margins = []

        for i in range(0, len(max_race_durations)):
            ways_to_beat_race = BoatRace._ways_to_beat_distance_record(max_race_durations[i], distance_records[i])
            all_error_margins.append(len(ways_to_beat_race))

        return math.prod(all_error_margins)
