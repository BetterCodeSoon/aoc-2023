from src.aoc3 import Coords
from src.aoc3.adjacent_cells import AdjacentCells


class Cell:

    def __init__(self, coords: Coords, element: str, adjacent_cells: AdjacentCells):

        if coords is None:
            raise ValueError("Coordinates are None!")

        if element is None:
            raise ValueError("The cell element is None!")

        if len(element) != 1:
            raise ValueError(f"A cell needs to have exactly ONE element. The elem: {element} is invalid!")

        if adjacent_cells is None:
            raise ValueError("The adjacent cells object is None!")

        self.coords: Coords = coords
        self.element: str = element
        self.adjacent_cells: AdjacentCells = adjacent_cells

    def is_digit(self):
        return self.element.isdigit()

    def is_period(self):
        return self.element == "."

    def is_symbol(self):
        if self.is_period() or self.is_digit():
            return False
        return True

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return (self.element == other.element
                and self.coords == other.coords
                and self.adjacent_cells == other.adjacent_cells)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.coords, self.element, self.adjacent_cells))
