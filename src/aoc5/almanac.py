from src.aoc5.source_destination_map import SourceDestinationMap


class Almanac:

    def __init__(self, seeds: [int], maps_lines: [str]):
        if seeds is None:
            raise ValueError("Seed list being None is no bueno! :(\n")
        if maps_lines is None:
            raise ValueError("Maps strings are None!\n")

        self.seeds = seeds
        self.almanac_dict: {(str, str): SourceDestinationMap} = self._generate_almanac_dicts(maps_lines)

    @staticmethod
    def _generate_almanac_dicts(maps_line_strs: [str]) -> {(str, str): SourceDestinationMap}:

        # List of maps.
        # {dest: list index to get source_dest_map to that destination}
        # {source: list index to get source_dest_map for that source}

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
