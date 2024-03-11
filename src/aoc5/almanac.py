from src.aoc5.source_destination_map import SourceDestinationMap


class Almanac:

    def __init__(self, seeds: [int], maps_lines: [str]):
        if seeds is None:
            raise ValueError("Seed list being None is no bueno! :(\n")
        if maps_lines is None:
            raise ValueError("Maps strings are None!\n")

        self.seeds = seeds
        self.almanac_dict: {(str, str): SourceDestinationMap} = self._generate_almanac_dicts(maps_lines)
        self.seed_ranges = self._seed_ranges(seeds)

    @staticmethod
    def _generate_almanac_dicts(maps_line_strs: [str]) -> {(str, str): SourceDestinationMap}:

        almanac_dict: {(str, str): SourceDestinationMap} = {}

        for map_str in maps_line_strs:
            sd_map = SourceDestinationMap(map_str)
            almanac_dict[(sd_map.source_name, sd_map.destination_name)] = sd_map

        return almanac_dict

    def get_seed_to_location(self, seed: int):

        key_tuple_list: (str, str) = [("seed", "soil"),
                                      ("soil", "fertilizer"),
                                      ("fertilizer", "water"),
                                      ("water", "light"),
                                      ("light", "temperature"),
                                      ("temperature", "humidity"),
                                      ("humidity", "location")]

        current_source_number = seed

        for key_tuple in key_tuple_list:
            sd_map: SourceDestinationMap = self.almanac_dict[key_tuple]
            current_source_number = sd_map.destination_number(current_source_number)

        return current_source_number

    def lowest_location_number(self):
        return min([self.get_seed_to_location(seed) for seed in self.seeds])

    @staticmethod
    def _seed_ranges(seeds: [int]):
        return [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    def lowest_location_over_seed_ranges(self):
        current_min_location = None
        print(f"Starting to process.. there are {len(self.seed_ranges)} seed tupples in total. \n\n")
        count = 0

        for seed_tuple in self.seed_ranges:
            count += 1
            print(f"Processing tuple: {count}..\n")
            seed_start = seed_tuple[0]
            seed_end = seed_start + seed_tuple[1] - 1
            current_min_location = self.min_location_for_seed_range(current_min_location, seed_start, seed_end)

        print(f"..100% done - lowest location was: {current_min_location}\n")
        return current_min_location

    def min_location_for_seed_range(self, current_min_location, seed_start, seed_end):
        total_seeds = seed_end - seed_start
        print(f"Oh boy. Total seed numbers to process: {total_seeds}\n")
        current_iteration = 1
        percentage_milestone = 0

        for seed_number in range(seed_start, seed_end):
            location_number = self.get_seed_to_location(seed_number)

            if current_min_location is None:
                current_min_location = location_number

            current_min_location = min(location_number, current_min_location)
            percentage_milestone = self.show_progress(current_iteration, total_seeds, percentage_milestone)
            current_iteration += 1

        return current_min_location

    @staticmethod
    def show_progress(iteration: int, total: int, percentage_milestone: int):
        progress = int((iteration / total) * 100)

        if percentage_milestone == 0 and 20 <= progress <= 30:
            percentage_milestone = 1
            print(f"..25% ", end=' ')
        if percentage_milestone == 1 and 45 <= progress <= 55:
            print(f"..50% ", end=' ')
            percentage_milestone = 2
        if percentage_milestone == 2 and 75 <= progress <= 80:
            print(f"..75% ", end=' ')
            percentage_milestone = 3

        return percentage_milestone
