from deprecated import deprecated

from src.aoc8.day8_input_reader import Day8InputReader
from src.aoc8.network import Network
from src.utils import benchmark_helper
from src.utils.input.puzzle_input_file import PuzzleInputFile


def solve_part1(input_reader: Day8InputReader):
    # Day8 Solution Part 1:
    network_1 = Network(input_reader.path, input_reader.network_dict)
    steps = network_1.part1_steps_to_zzz()
    print(f"Part1: It took {steps} to reach ZZZ! \n\n")


@deprecated(reason="The brute force solution will get entangled in cycles and takes forever to calc")
def solve_part2_brute_force_threadpool(input_reader: Day8InputReader):
    # Day8 Solution Part 2:
    network_2 = Network(input_reader.path, input_reader.network_dict)
    print(f"\n\nPart2: Starting with {len(network_2.current_nodes)}-starting nodes ...\n\n")
    count = network_2.calc_part2_brute_force_threadpool()
    print(f"it took {count} steps to reach a state where all nodes end with Z\n\n"
          f"Final Nodes:\n{network_2.current_nodes}")


if __name__ == '__main__':
    puzzle_file = PuzzleInputFile(8, 1, '#', "")
    day8_input_reader = Day8InputReader(puzzle_file)

    benchmark_helper.benchmark(solve_part1, day8_input_reader)
    # benchmark_helper.benchmark(solve_part2_brute_force_threadpool, day8_input_reader)
