from src import TYPE_PUZZLE
from src.aoc5.almanac import Almanac
from src.aoc5.day5_input_reader import Day5InputReader
from src.utils.input.input_file import InputFile

if __name__ == '__main__':
    puzzle_file = InputFile(TYPE_PUZZLE, 5, 1, "#", False)
    input_reader = Day5InputReader(puzzle_file)

    print(f"Lowest location number = "
          f"{Almanac(input_reader.seeds, input_reader.maps_str_list).lowest_location_number()} \n")
