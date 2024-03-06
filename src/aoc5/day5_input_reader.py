from src.utils.input.input_file import InputFile
from utils.string_helper import to_int


class Day5InputReader:

    def __init__(self, input_file: InputFile):
        if input_file is None:
            raise ValueError("Danger eek! The input file is None!!\n")

        file_lines = input_file.file_lines
        self.seeds: [int] = self.collect_seeds(file_lines[0])

        maps_lines: [str] = file_lines[2:]
        self.maps_str_list = self.collect_maps(maps_lines)

    @staticmethod
    def collect_seeds(seeds_str: str) -> [int]:
        return to_int(seeds_str.split(":")[1].lstrip().split(" "))

    @staticmethod
    def collect_maps(maps_lines: [str]) -> [[str]]:
        last_line_index = len(maps_lines) - 1
        maps_str_list: [[str]] = []
        current_map_list = []

        for index, line in enumerate(maps_lines):
            if line[0].isalpha():
                # map title
                current_map_list.append(line.rstrip()[:-5])
            if line[0].isdigit():
                # source, destination numbers
                current_map_list.append(line.rstrip())
            if line[0] == "\n" or index == last_line_index:
                # end of the map so save it and reset current map
                maps_str_list.append(current_map_list)
                current_map_list = []

        return maps_str_list
