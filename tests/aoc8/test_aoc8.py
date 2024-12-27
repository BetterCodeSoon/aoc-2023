from src.aoc8.network import Network
from src.aoc8.day8_input_reader import Day8InputReader
from src.utils.input.puzzle_input_file import PuzzleInputFile


class TestAoc8:

    def test_aoc8(self):
        puzzle_file = PuzzleInputFile(8, 1, '#', " ")
        day8_input_reader = Day8InputReader(puzzle_file)
        network = Network(day8_input_reader.path, day8_input_reader.network_dict)
        assert network.steps_to_zzz() == 14257
