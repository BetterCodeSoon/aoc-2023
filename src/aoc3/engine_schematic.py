from src.aoc3 import Coords
from src.aoc3.adjacent_cells import AdjacentCells
from src.aoc3.cell import Cell
from src.aoc3.schematic_number import SchematicNumber
from src.utils.input.input_line import InputLine


class EngineSchematic:

    def __init__(self, input_lines: [InputLine]):
        if input_lines is None:
            raise ValueError("Ahhh panic! Cannot create EngineSchematic if the input is None!! :(")

        self.max_x_index: int = self._calc_max_x_index(input_lines)
        self.max_y_index: int = self._calc_max_y_index(input_lines)
        self.cell_dict: {Coords: Cell} = {}
        self.numbers_dict: {int: [SchematicNumber]} = {}  # {y coordinate: [Schematic Number]}
        self.cell_dict, self.numbers_dict = self._create_cells_from_input_lines(input_lines)
        self.part_numbers: [SchematicNumber] = self._find_part_numbers()

    def _create_cells_from_input_lines(self, input_lines: [InputLine]) -> ({Coords: Cell}, {int: [SchematicNumber]}):
        cell_dict: {Coords: Cell} = {}
        numbers_dict: {int: [SchematicNumber]} = {}

        # go through each row from start to end
        for y in range(self.max_y_index + 1):
            for x in range(self.max_x_index + 1):

                element = self._element_from_input(x, input_lines[y])
                coords = Coords(x, y)
                cell_dict[coords] = self._cell(coords, element)

                if coords.y not in numbers_dict:
                    numbers_dict[coords.y] = []

                if element.isdigit():
                    numbers_dict[coords.y] = self._add_number(coords, element, numbers_dict[coords.y])

        return cell_dict, numbers_dict

    def _add_number(self, coords: Coords, element: str, numbers_list: [SchematicNumber]) -> [SchematicNumber]:
        adjacent_cells = AdjacentCells(coords, self.max_x_index, self.max_x_index)
        new_cell = Cell(coords, element, adjacent_cells)
        new_number = SchematicNumber([new_cell])

        # check if there is a number in numbers_list
        if len(numbers_list) == 0:
            # if its empty then just add the number
            numbers_list.append(new_number)
            return numbers_list

        # otherwise..
        last_number: SchematicNumber = numbers_list[-1]
        last_digit_cell: Cell = last_number.cells[-1]
        # take the last number from the numbers list and check if its next to the current digit
        if last_digit_cell.coords.x == (coords.x - 1) and last_digit_cell.coords.y == coords.y:
            # if that's the case add the cell to the existing number
            last_number.add_cell(new_cell)
            numbers_list[-1] = last_number
            return numbers_list
        else:
            # otherwise add a new number to the list of numbers
            numbers_list.append(new_number)
            return numbers_list

    def adjacent_to_symbol(self, number: SchematicNumber):
        # check all adjacent cells for each digit
        number_cells: [Cell] = number.cells
        return any(self._any_cell_adjacent_to_symbol(cell.adjacent_cells) for cell in number_cells)

    def _any_cell_adjacent_to_symbol(self, adjacent_cells: AdjacentCells):
        return any(self.cell_dict[coords].is_symbol() for coords in adjacent_cells.possible_adjacent_cells.values())

    def get_all_number_values(self) -> [int]:
        return [number.value for schematic_num_list in self.numbers_dict.values() for number in schematic_num_list]

    def _find_part_numbers(self) -> [SchematicNumber]:
        return [number for schematic_num_list in self.numbers_dict.values() for number in
                schematic_num_list if self.adjacent_to_symbol(number)]

    def get_all_part_number_values(self) -> [int]:
        return [number.value for number in self.part_numbers]

    def _cell(self, coords: Coords, element: str) -> Cell:
        return Cell(coords, element, AdjacentCells(coords, self.max_x_index, self.max_y_index))

    @staticmethod
    def _element_from_input(x: int, input_line: InputLine) -> str:
        return input_line.line_str[x]

    @staticmethod
    def _calc_max_x_index(input_lines: [InputLine]) -> int:
        max_columns = len(input_lines)
        if max_columns < 1:
            raise ValueError(f"The number of columns={max_columns} is too small!")
        return max_columns - 1

    @staticmethod
    def _calc_max_y_index(input_lines: [InputLine]) -> int:
        max_rows = len(input_lines[0].line_str)
        if max_rows < 1:
            raise ValueError(f"The number of rows={max_rows} is too small!")
        return max_rows - 1
