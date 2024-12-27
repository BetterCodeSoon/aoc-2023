from src.aoc8.network import Network
from src.aoc8.day8_input_reader import Day8InputReader
from src.utils.input.puzzle_input_file import PuzzleInputFile

if __name__ == '__main__':
    puzzle_file = PuzzleInputFile(8, 1, '#', "")
    day8_input_reader = Day8InputReader(puzzle_file)

    # Day8 Solution Part 1:

    network = Network(day8_input_reader.path, day8_input_reader.network_dict)
    steps = network.steps_to_zzz()

    print(f"It took {steps} to reach ZZZ! \n\n")
