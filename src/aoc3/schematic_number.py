from src.aoc3.cell import Cell


class SchematicNumber:

    def __init__(self, cells: [Cell]):
        if cells is None:
            raise ValueError("The list of Cells is None!")

        if len(cells) < 1:
            raise ValueError("A number must contain at least one digit")

        self.row_y = cells[0].coords.y
        [self._validate_cell(cell) for cell in cells]

        self.cells: [Cell] = cells
        self._update_value()

    def _validate_cell(self, cell: Cell):
        if cell.coords.y != self.row_y:
            raise ValueError(
                f"A number can only be formed by digits on the same row.\n"
                f"But for cell: {cell} coords.y = {cell.coords.y} instead of {self.row_y}\n")
        if not cell.is_digit():
            raise ValueError(
                f"A cell belonging to a number needs to contain a digit and not cell.elem: {cell.element}")

    def add_cell(self, cell: Cell):
        # only allow to add number cell right next to the existing cell
        if cell.coords.x != (self.cells[-1].coords.x + 1):
            raise ValueError(f"It is only possible to add a cell with digit to the right of an existing digit!\n"
                             f"Last cell x-coord: {self.cells[-1].coords.x}\n"
                             f"Cell that is supposed to be added x-coord: {cell.coords.x}")
        self._validate_cell(cell)
        self.cells.append(cell)
        self._update_value()

    def _update_value(self):
        self.value: int = int("".join(cell.element for cell in self.cells))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return self.row_y == self.cells == other.cells and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.row_y, tuple(self.cells), self.value))
