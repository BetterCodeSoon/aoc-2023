from aoc5.almanac import Almanac
from aoc5.day5_input_reader import Day5InputReader
from src import TYPE_PUZZLE
from utils.input.input_file import InputFile


class TestAoc5:

    def test_aoc5(self):
        expected_lowest_location_number = 457535844

        puzzle_file = InputFile(TYPE_PUZZLE, 5, 1, "#", False)
        input_reader = Day5InputReader(puzzle_file)
        almanac = Almanac(input_reader.seeds, input_reader.maps_str_list)
        assert almanac.lowest_location_number() == expected_lowest_location_number
        # this test takes like 24h in the current implementation
        # toDo: perhaps refactor solution to be more efficient at some point
        # assert almanac.lowest_location_over_seed_ranges() == 41222968
