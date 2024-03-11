import pytest

from src.aoc5.day5_input_reader import Day5InputReader
from tests.aoc5 import tcase1_file_lines


class TestDay5InputReader:

    @pytest.mark.parametrize("input_str, expected_seeds_list", [
        ("seeds: 79 14 55 13", [79, 14, 55, 13])
    ])
    def test_seeds(self, input_str, expected_seeds_list):
        assert Day5InputReader._collect_seeds(input_str) == expected_seeds_list

    @pytest.mark.parametrize("input_lines, expected_maps_list", [
        (tcase1_file_lines()[2:],
         [['seed-to-soil', '50 98 2', '52 50 48'],
          ['soil-to-fertilizer', '0 15 37', '37 52 2', '39 0 15'],
          ['fertilizer-to-water', '49 53 8', '0 11 42', '42 0 7', '57 7 4'],
          ['water-to-light', '88 18 7', '18 25 70'],
          ['light-to-temperature', '45 77 23', '81 45 19', '68 64 13'],
          ['temperature-to-humidity', '0 69 1', '1 0 69'],
          ['humidity-to-location', '60 56 37', '56 93 4']])
    ])
    def test_collect_maps(self, input_lines, expected_maps_list):
        assert Day5InputReader._collect_maps(input_lines) == expected_maps_list
