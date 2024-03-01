import pytest

from src.aoc3 import Coords
from src.aoc3.adjacent_cells import AdjacentCells
from src.aoc3.cell import Cell
from tests.aoc3.test_adjacent_cells import ADJACENT_CELLS_DICT


def create_cell(x: int, y: int, elem: str) -> Cell:
    coords = Coords(x, y)
    return Cell(coords, elem, AdjacentCells(coords, 2, 2))


class TestCell:
    max_x = 2
    max_y = 2
    coords1 = Coords(1, 1)
    coords2 = Coords(2, 2)

    @pytest.mark.parametrize("coords, elem, adjacent_cells", [(coords1, ".", ADJACENT_CELLS_DICT[coords1])])
    def test_initialization(self, coords, elem, adjacent_cells):
        cell = Cell(coords, elem, adjacent_cells)
        assert cell.coords == coords
        assert cell.element == elem
        assert cell.adjacent_cells == adjacent_cells

    @pytest.mark.parametrize("cell1, cell2, expected",
                             [
                                 (Cell(coords1, ".", AdjacentCells(coords1, max_x, max_y)),
                                  Cell(coords1, ".", AdjacentCells(coords1, max_x, max_y)), True),
                                 (Cell(coords1, ".", AdjacentCells(coords1, max_x, max_y)),
                                  Cell(coords2, "1", AdjacentCells(coords2, max_x, max_y)), False)
                             ])
    def test_equality(self, cell1, cell2, expected):
        assert (cell1 == cell2) == expected

    @pytest.mark.parametrize("cell1, cell2, expected",
                             [
                                 (Cell(coords1, ".", AdjacentCells(coords1, max_x, max_y)),
                                  Cell(coords1, ".", AdjacentCells(coords1, max_x, max_y)), False),
                                 (Cell(coords1, ".", AdjacentCells(coords1, max_x, max_y)),
                                  Cell(coords2, "1", AdjacentCells(coords2, max_x, max_y)), True)
                             ])
    def test_inequality(self, cell1, cell2, expected):
        assert (cell1 != cell2) == expected

    def test_is_digit(self):
        assert create_cell(1, 1, "2").is_digit()
        assert not create_cell(1, 2, ".").is_digit()

    def test_is_period(self):
        assert not create_cell(1, 1, "2").is_period()
        assert create_cell(1, 2, ".").is_period()

    def test_is_symbol(self):
        assert create_cell(1, 1, "2").is_symbol()
        assert create_cell(1, 1, "#").is_symbol()
        assert not create_cell(1, 2, ".").is_symbol()

    def test_hash(self):
        coords = Coords(1, 1)
        adjacent_cells = AdjacentCells(coords, 2, 2)
        elem = "."
        assert Cell(coords, elem, adjacent_cells).__hash__() == hash((coords, elem, adjacent_cells))
