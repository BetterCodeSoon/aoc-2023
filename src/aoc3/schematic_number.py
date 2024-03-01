from src.aoc3.cell import Cell


class SchematicNumber:

    def __init__(self, cells: [Cell]):
        if cells is None:
            raise ValueError("The list of Cells is None!")

        if len(cells) < 1:
            raise ValueError("A number must contain at least one digit")

        x = cells[0].coords.x
        for cell in cells:
            if cell.coords.x != x:
                raise ValueError(
                    f"A number can only be formed by digits on the same row.\n"
                    f"But for cell: {cell} coords.x = {cell.coords.x} instead of {x}\n")
            if not cell.is_digit():
                raise ValueError(
                    f"A cell belonging to a number needs to contain a digit and not cell.elem: {cell.element}")

        self.cells: [Cell] = cells
        self.value: int = int("".join(cell.element for cell in cells))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return self.cells == other.cells and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((tuple(self.cells), self.value))
