import pytest

from src.aoc5.almanac import Almanac
from src.aoc5.day5_input_reader import Day5InputReader
from tests.aoc5 import read_tcase1_file


class TestAlmanac:
    input_reader = Day5InputReader(read_tcase1_file())
    almanac = Almanac(input_reader.seeds, input_reader.maps_str_list)

    @pytest.mark.parametrize("input_seed_number, expected_location_number",
                             [(79, 82), (14, 43), (55, 86), (13, 35)])
    def test_get_seed_to_location(self, input_seed_number, expected_location_number):
        assert self.almanac.get_seed_to_location(input_seed_number) == expected_location_number

    def test_lowest_location_number(self):
        # seeds: [79, 14, 55, 13]
        assert self.almanac.lowest_location_number() == 35

    @pytest.mark.skip("Test needs implementation of SourceDestinationMap equals op")
    @pytest.mark.parametrize("input_map_str_list, expected_dict", [
        ([['seed-to-soil', '50 98 2', '52 50 2'],
          ['soil-to-fertilizer', '0 15 2', '37 52 2', '39 0 2']],
         {('seed', 'soil'): {50: 52, 51: 53, 98: 50, 99: 51},
          ('soil', 'fertilizer'): {0: 39, 1: 40, 15: 0, 16: 1, 52: 37, 53: 38}})
    ])
    def test_generate_almanac_dicts(self, input_map_str_list, expected_dict):
        assert Almanac._generate_almanac_dicts(input_map_str_list) == expected_dict
