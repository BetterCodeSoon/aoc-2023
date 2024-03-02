from src.aoc3.engine_schematic import EngineSchematic
from src.utils.input.puzzle_input_file import PuzzleInputFile


class TestAoc3:

    def test_correct_solution_a(self):
        puzzle_file = PuzzleInputFile(3, 1, "#")
        engine_schematic = EngineSchematic(puzzle_file.puzzle_input_lines)
        assert sum(engine_schematic.get_all_part_number_values()) == 551094
