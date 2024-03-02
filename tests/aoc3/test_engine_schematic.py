import pytest

from src.aoc3.engine_schematic import EngineSchematic
from src.utils.input.input_line import InputLine
from src.utils.input.testcase_input_file import TestcaseInputFile


def testcase_input_file(day, number) -> TestcaseInputFile:
    return TestcaseInputFile(day, number, "~", "|", ',')


def testcase_input_lines(day: int, number: int) -> [InputLine]:
    return testcase_input_file(day, number).testcase_input_lines


def testcase_expected_values(day: int, number: int) -> [[str]]:
    return testcase_input_file(day, number).testcase_expected_values


def flat_int_list(value_list: [[str]]) -> [int]:
    return [int(value) for sublist in value_list for value in sublist if value != '']


class TestEngineSchematic:
    # x = 10 * y = 10 input, part numbers are in expected values for each row
    testcase_1_input_lines: [InputLine] = testcase_input_lines(3, 1)
    testcase_1_expected_values: [[str]] = testcase_expected_values(3, 1)

    # testcase to find ALL numbers (independent whether they are part number or not)
    testcase_2_input_lines: [InputLine] = testcase_input_lines(3, 2)
    testcase_2_expected_values: [[str]] = testcase_expected_values(3, 2)

    @pytest.mark.parametrize("input_lines, expected_max_x, expected_max_y, expected_numbers, expected_part_numbers", [
        (testcase_2_input_lines, 9, 9, flat_int_list(testcase_2_expected_values),
         flat_int_list(testcase_1_expected_values))
    ])
    def test_initialization(self, input_lines, expected_max_x, expected_max_y, expected_numbers, expected_part_numbers):
        engine_schematic = EngineSchematic(input_lines)
        assert engine_schematic.max_x_index == expected_max_x
        assert engine_schematic.max_y_index == expected_max_y

        engine_numbers = engine_schematic.get_all_number_values()
        assert engine_numbers == expected_numbers

        part_numbers = engine_schematic.get_all_part_number_values()
        assert part_numbers == expected_part_numbers
        # no need to test for correct cell_dict or num_dict when the correct part numbers are calculated
        # assert engine_schematic.cell_dict == expected_cell_dict
        # assert engine_schematic.numbers_dict == expected_num_dict

    @pytest.mark.parametrize("input_lines, expected", [(testcase_1_input_lines, 9)])
    def test_calc_max_rows(self, input_lines: [InputLine], expected):
        assert EngineSchematic._calc_max_y_index(input_lines) == expected

    @pytest.mark.parametrize("input_lines, expected", [(testcase_1_input_lines, 9)])
    def test_calc_max_columns(self, input_lines: [InputLine], expected):
        assert EngineSchematic._calc_max_x_index(input_lines) == expected
