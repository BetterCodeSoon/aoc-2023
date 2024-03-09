import pytest

from src.aoc5.source_destination_map import SourceDestinationMap


class TestSourceDestinationMap:

    @pytest.mark.parametrize("input_map_list, map_name, expected_src_name, expected_dest_name, expected_dict", [
        (['seed-to-soil', '50 98 2', '52 50 5'], "seed-to-soil", "seed", "soil",
         [(98, 50, 2, 99, 51), (50, 52, 5, 54, 56)])
    ])
    def test_initialization(self, input_map_list, map_name, expected_src_name, expected_dest_name, expected_dict):
        almanac_map = SourceDestinationMap(input_map_list)
        assert almanac_map.map_name == map_name
        assert almanac_map.source_name == expected_src_name
        assert almanac_map.destination_name == expected_dest_name
        assert almanac_map.src_to_dest_list == expected_dict

    @pytest.mark.parametrize("input_range_list, expected_map", [
        ([50, 98, 2], (98, 50, 2, 99, 51))

    ])
    def test_generate_mapping_from_line(self, input_range_list, expected_map):
        assert SourceDestinationMap._generate_mapping_from_line(input_range_list) == expected_map

    @pytest.mark.parametrize("input_ranges_str_list, expected_dict", [
        (['50 98 2', '52 50 4'],
         [(98, 50, 2, 99, 51), (50, 52, 4, 53, 55)])
    ])
    def test_generate_mapping_from_ranges_list(self, input_ranges_str_list, expected_dict):
        assert SourceDestinationMap._generate_mapping_from_ranges_list(input_ranges_str_list) == expected_dict

    @pytest.mark.parametrize("input_map_list, input_src_number,  expected_dest_num", [
        (['seed-to-soil', '50 98 2', '52 50 48'], 1000, 1000),
        (['seed-to-soil', '50 98 2', '52 50 48'], 98, 50),
        (['seed-to-soil', '50 98 2', '52 50 48'], 54, 56)
    ])
    def test_destination_number(self, input_src_number, input_map_list, expected_dest_num):
        assert SourceDestinationMap(input_map_list).destination_number(input_src_number) == expected_dest_num

    @pytest.mark.parametrize("input_str, expected_source, expected_destination", [("seed-to-soil", "seed", "soil")])
    def test_source_destination(self, input_str, expected_source, expected_destination):
        assert SourceDestinationMap._source_destination_names(input_str) == [expected_source, expected_destination]

    @pytest.mark.parametrize("input_str, expected_dest_range_start, expected_src_range_start, expected_range_len",
                             [("50 98 2", 50, 98, 2), ("52 50 48", 52, 50, 48)])
    def test_process_range_line_str(self, input_str, expected_dest_range_start, expected_src_range_start,
                                    expected_range_len):
        assert SourceDestinationMap._process_range_line_str(input_str) == [expected_dest_range_start,
                                                                           expected_src_range_start,
                                                                           expected_range_len]
