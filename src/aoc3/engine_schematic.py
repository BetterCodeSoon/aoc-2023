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
        self._determine_gears()

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

    def get_gear_ratios(self) -> [int]:
        return [self.gears_dict[gear][0] for gear in self.gears_dict.keys()]

    def _determine_gears(self):
        # {Coords to the Gear: {SchematicNumbers adjacent to it: their int value}}
        self.gears_dict: {Coords: (int, {SchematicNumber: int})} = {}
        # go through each row from start to end
        for y in range(self.max_y_index + 1):
            for x in range(self.max_x_index + 1):

                coords = Coords(x, y)
                current_cell = self.cell_dict[coords]

                if self._is_star(current_cell.element):

                    # collect all numbers that are adjacent to '*'
                    current_num_dict = self._check_for_adjacent_numbers(current_cell)
                    if len(current_num_dict) == 2:
                        gear_ratio = self._calc_gear_ratio(current_num_dict)
                        self.gears_dict[current_cell.coords] = (gear_ratio, current_num_dict)

    @staticmethod
    def _is_star(element: str):
        if element == "*":
            return True
        return False

    def _check_for_adjacent_numbers(self, current_cell: Cell):
        # {SchematicNumber: the numbers value}
        adjacent_numbers_dict: {SchematicNumber: int} = {}

        # get the coords of all adjacent cells
        adjacent_numbers_coords = [coord for coord in current_cell.adjacent_cells.possible_adjacent_cells.values()]
        adjacent_number_cells = [self.cell_dict[coord] for coord in adjacent_numbers_coords]

        for cell in adjacent_number_cells:
            adjacent_num = self._is_number_cell(cell)

            if adjacent_num is not None:
                adjacent_numbers_dict[adjacent_num] = adjacent_num.value
        return adjacent_numbers_dict

    def _is_number_cell(self, cell: Cell) -> SchematicNumber:
        # cell belongs to number? return number
        numbers_list: [SchematicNumber] = self.numbers_dict[cell.coords.y]
        for number in numbers_list:
            if cell in number.cells:
                return number

    @staticmethod
    def _calc_gear_ratio(current_num_dict: {SchematicNumber: int}):
        if len(current_num_dict) != 2:
            raise ValueError(f"The gear ratio can only be calculated from exactly two numbers. "
                             f"But length of current_num_dict is = {len(current_num_dict)}")
        number_values = list(current_num_dict.values())
        return number_values[0] * number_values[1]

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
