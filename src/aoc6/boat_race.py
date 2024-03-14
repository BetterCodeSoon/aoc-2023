import math

from src.aoc6.boat import Boat


class BoatRace:

    @staticmethod
    def _ways_to_beat_distance_record(max_race_duration: int, distance_record: int) -> [int]:
        ways_to_beat_record: [int] = []

        for time_button_pressed in range(0, max_race_duration):
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

    @staticmethod
    def find_minimum_way(max_race_duration: int, distance_record: int) -> int:
        for time_button_pressed in range(0, max_race_duration):
            distanced_travelled = Boat.calc_distance(time_button_pressed, max_race_duration)
            if distanced_travelled > distance_record:
                return time_button_pressed
        return 0

    @staticmethod
    def find_maximum_way(max_race_duration: int, distance_record: int) -> int:
        for time_button_pressed in range(max_race_duration, -1, -1):
            distance_travelled = Boat.calc_distance(time_button_pressed, max_race_duration)
            if distance_travelled > distance_record:
                return time_button_pressed
        return 0

    @staticmethod
    def ways_by_min_max(max_race_duration: int, distance_record: int) -> int:
        min_time_button_pressed = BoatRace.find_minimum_way(max_race_duration, distance_record)
        max_time_button_pressed = BoatRace.find_maximum_way(max_race_duration, distance_record)
        return (max_time_button_pressed - min_time_button_pressed) + 1
