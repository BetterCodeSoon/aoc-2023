from src.aoc3.engine_schematic import EngineSchematic
from src.utils.input.puzzle_input_file import PuzzleInputFile

if __name__ == '__main__':
    puzzle_file = PuzzleInputFile(3, 1, "#")
    engine_schematic = EngineSchematic(puzzle_file.puzzle_input_lines)

    print(
        f"The sum of all part numbers in the engine schematic = {sum(engine_schematic.get_all_part_number_values())}\n")

    print(f"And the sum of all gear ratios = {sum(engine_schematic.get_gear_ratios())} ")
