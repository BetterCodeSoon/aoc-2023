import pytest

from src.aoc3 import Coords
from src.aoc3.adjacent_cells import AdjacentCells


class TestAdjacentCells:
    max_x: int = 2
    max_y: int = 2

    @pytest.mark.parametrize("current_coord, expected_adjacent_cells",
                             [
                                 (Coords(1, 0),
                                  {1: Coords(x=0, y=1), 2: Coords(x=1, y=1), 3: Coords(x=2, y=1),
                                   4: Coords(x=0, y=0), 6: Coords(x=2, y=0)}),
                                 (Coords(0, 0),
                                  {2: Coords(x=0, y=1), 3: Coords(x=1, y=1), 6: Coords(x=1, y=0)}),
                                 (Coords(max_x, 0),
                                  {1: Coords(x=1, y=1), 2: Coords(x=2, y=1), 4: Coords(x=1, y=0)}),
                                 (Coords(0, max_y),
                                  {6: Coords(x=1, y=2), 8: Coords(x=0, y=1), 9: Coords(x=1, y=1)}),
                                 (Coords(max_x, max_y),
                                  {4: Coords(x=1, y=2), 7: Coords(x=1, y=1), 8: Coords(x=2, y=1)}),
                                 (Coords(1, 1),
                                  {1: Coords(x=0, y=2), 2: Coords(x=1, y=2), 3: Coords(x=2, y=2), 4: Coords(x=0, y=1),
                                   6: Coords(x=2, y=1), 7: Coords(x=0, y=0), 8: Coords(x=1, y=0),
                                   9: Coords(x=2, y=0)}),
                                 (Coords(0, 1),
                                  {2: Coords(x=0, y=2), 3: Coords(x=1, y=2), 6: Coords(x=1, y=1), 8: Coords(x=0, y=0),
                                   9: Coords(x=1, y=0)}),
                                 (Coords(max_x, 1),
                                  {1: Coords(x=1, y=2), 2: Coords(x=2, y=2), 4: Coords(x=1, y=1),
                                   7: Coords(x=1, y=0), 8: Coords(x=2, y=0)}),
                                 (Coords(1, max_y),
                                  {4: Coords(x=0, y=2), 6: Coords(x=2, y=2), 7: Coords(x=0, y=1), 8: Coords(x=1, y=1),
                                   9: Coords(x=2, y=1)})
                             ])
    def test_initialization(self, current_coord, expected_adjacent_cells):
        assert AdjacentCells(current_coord, self.max_x, self.max_y).possible_adjacent_cells == expected_adjacent_cells

    @pytest.mark.parametrize("adjacent_cell1, adjacent_cell2, expected",
                             [
                                 (AdjacentCells(Coords(1, 1), max_x, max_y), AdjacentCells(Coords(1, 1), max_x, max_y),
                                  True),
                                 (AdjacentCells(Coords(1, 1), max_x, max_y), AdjacentCells(Coords(2, 2), max_x, max_y),
                                  False)
                             ])
    def test_equality(self, adjacent_cell1, adjacent_cell2, expected):
        assert (adjacent_cell1 == adjacent_cell2) == expected

    @pytest.mark.parametrize("adjacent_cell1, adjacent_cell2, expected",
                             [
                                 (AdjacentCells(Coords(1, 1), max_x, max_y), AdjacentCells(Coords(1, 1), max_x, max_y),
                                  False),
                                 (AdjacentCells(Coords(1, 1), max_x, max_y), AdjacentCells(Coords(2, 2), max_x, max_y),
                                  True)
                             ])
    def test_inequality(self, adjacent_cell1, adjacent_cell2, expected):
        assert (adjacent_cell1 != adjacent_cell2) == expected

    def test_hash(self):
        assert AdjacentCells(Coords(0, 0), self.max_x, self.max_y).__hash__() == hash(
            tuple({6: Coords(x=1, y=0), 2: Coords(x=0, y=1), 3: Coords(x=1, y=1)}))
