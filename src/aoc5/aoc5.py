from src import TYPE_PUZZLE
from src.aoc5.almanac import Almanac
from src.aoc5.day5_input_reader import Day5InputReader
from src.utils.input.input_file import InputFile

if __name__ == '__main__':
    puzzle_file = InputFile(TYPE_PUZZLE, 5, 1, "#", False)
    input_reader = Day5InputReader(puzzle_file)
    almanac = Almanac(input_reader.seeds, input_reader.maps_str_list)

    print(f"Lowest location number = "
          f"{almanac.lowest_location_number()} \n")

    print(
        f"However, checking the entire range of seeds gives the lowest location number = "
        f"{almanac.lowest_location_over_seed_ranges()}  \n")
