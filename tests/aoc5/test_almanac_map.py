import pytest

from src.aoc5.almanac_map import AlmanacMap


class TestAlmanacMap:

    @pytest.mark.parametrize("input_map_list, map_name, expected_src_name, expected_dest_name, expected_dict", [
        (['seed-to-soil', '50 98 2', '52 50 5'], "seed-to-soil", "seed", "soil",
         {50: 52, 51: 53, 52: 54, 53: 55, 54: 56, 98: 50, 99: 51})
    ])
    def test_initialization(self, input_map_list, map_name, expected_src_name, expected_dest_name, expected_dict):
        almanac_map = AlmanacMap(input_map_list)
        assert almanac_map.map_name == map_name
        assert almanac_map.source_name == expected_src_name
        assert almanac_map.destination_name == expected_dest_name
        assert almanac_map.src_to_dest_dict == expected_dict

    @pytest.mark.parametrize("input_range_list, expected_map", [
        ([50, 98, 2], {98: 50, 99: 51}),
        ([52, 50, 48],
         {50: 52, 51: 53, 52: 54, 53: 55, 54: 56, 55: 57, 56: 58, 57: 59, 58: 60, 59: 61, 60: 62, 61: 63, 62: 64,
          63: 65, 64: 66, 65: 67, 66: 68, 67: 69, 68: 70, 69: 71, 70: 72, 71: 73, 72: 74, 73: 75, 74: 76, 75: 77,
          76: 78, 77: 79, 78: 80, 79: 81, 80: 82, 81: 83, 82: 84, 83: 85, 84: 86, 85: 87, 86: 88, 87: 89, 88: 90,
          89: 91, 90: 92, 91: 93, 92: 94, 93: 95, 94: 96, 95: 97, 96: 98, 97: 99})
    ])
    def test_generate_mapping_from_line(self, input_range_list, expected_map):
        assert AlmanacMap._generate_mapping_from_line(input_range_list) == expected_map

    @pytest.mark.parametrize("input_ranges_str_list, expected_dict", [
        (['50 98 2', '52 50 4'], {50: 52, 51: 53, 52: 54, 53: 55, 98: 50, 99: 51})
    ])
    def test_generate_mapping_from_ranges_list(self, input_ranges_str_list, expected_dict):
        assert AlmanacMap._generate_mapping_from_ranges_list(input_ranges_str_list) == expected_dict

    @pytest.mark.parametrize("input_map_list, input_src_number,  expected_dest_num", [
        (['seed-to-soil', '50 98 2', '52 50 48'], 1000, 1000),
        (['seed-to-soil', '50 98 2', '52 50 48'], 98, 50),
        (['seed-to-soil', '50 98 2', '52 50 48'], 54, 56)
    ])
    def test_destination_number(self, input_src_number, input_map_list, expected_dest_num):
        assert AlmanacMap(input_map_list).destination_number(input_src_number) == expected_dest_num

    @pytest.mark.parametrize("input_str, expected_source, expected_destination", [("seed-to-soil", "seed", "soil")])
    def test_source_destination(self, input_str, expected_source, expected_destination):
        assert AlmanacMap._source_destination_names(input_str) == [expected_source, expected_destination]

    @pytest.mark.parametrize("input_str, expected_dest_range_start, expected_src_range_start, expected_range_len",
                             [("50 98 2", 50, 98, 2), ("52 50 48", 52, 50, 48)])
    def test_process_range_line_str(self, input_str, expected_dest_range_start, expected_src_range_start,
                                    expected_range_len):
        assert AlmanacMap._process_range_line_str(input_str) == [expected_dest_range_start, expected_src_range_start,
                                                                 expected_range_len]
