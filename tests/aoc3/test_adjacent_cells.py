import pytest

from src.aoc3 import Coords
from src.aoc3.adjacent_cells import AdjacentCells

MAX_X: int = 2
MAX_Y: int = 2

ADJACENT_CELLS_DICT = {
    Coords(1, 0): {1: Coords(x=0, y=1), 2: Coords(x=1, y=1), 3: Coords(x=2, y=1), 4: Coords(x=0, y=0),
                   6: Coords(x=2, y=0)},
    Coords(0, 0):
        {2: Coords(x=0, y=1), 3: Coords(x=1, y=1), 6: Coords(x=1, y=0)},
    Coords(MAX_X, 0):
        {1: Coords(x=1, y=1), 2: Coords(x=2, y=1), 4: Coords(x=1, y=0)},
    Coords(0, MAX_Y):
        {6: Coords(x=1, y=2), 8: Coords(x=0, y=1), 9: Coords(x=1, y=1)},
    Coords(MAX_X, MAX_Y):
        {4: Coords(x=1, y=2), 7: Coords(x=1, y=1), 8: Coords(x=2, y=1)},
    Coords(1, 1):
        {1: Coords(x=0, y=2), 2: Coords(x=1, y=2), 3: Coords(x=2, y=2), 4: Coords(x=0, y=1),
         6: Coords(x=2, y=1), 7: Coords(x=0, y=0), 8: Coords(x=1, y=0),
         9: Coords(x=2, y=0)},
    Coords(0, 1):
        {2: Coords(x=0, y=2), 3: Coords(x=1, y=2), 6: Coords(x=1, y=1), 8: Coords(x=0, y=0),
         9: Coords(x=1, y=0)},
    Coords(MAX_X, 1):
        {1: Coords(x=1, y=2), 2: Coords(x=2, y=2), 4: Coords(x=1, y=1),
         7: Coords(x=1, y=0), 8: Coords(x=2, y=0)},
    Coords(1, MAX_Y):
        {4: Coords(x=0, y=2), 6: Coords(x=2, y=2), 7: Coords(x=0, y=1), 8: Coords(x=1, y=1),
         9: Coords(x=2, y=1)}
}


class TestAdjacentCells:

    @pytest.mark.parametrize("current_coord, expected_adjacent_cells",
                             [
                                 (Coords(1, 0), ADJACENT_CELLS_DICT[Coords(1, 0)]),
                                 (Coords(0, 0), ADJACENT_CELLS_DICT[Coords(0, 0)]),
                                 (Coords(MAX_X, 0), ADJACENT_CELLS_DICT[Coords(MAX_X, 0)]),
                                 (Coords(0, MAX_Y), ADJACENT_CELLS_DICT[Coords(0, MAX_Y)]),
                                 (Coords(MAX_X, MAX_Y), ADJACENT_CELLS_DICT[Coords(MAX_X, MAX_Y)]),
                                 (Coords(1, 1), ADJACENT_CELLS_DICT[Coords(1, 1)]),
                                 (Coords(0, 1), ADJACENT_CELLS_DICT[Coords(0, 1)]),
                                 (Coords(MAX_X, 1), ADJACENT_CELLS_DICT[Coords(MAX_X, 1)]),
                                 (Coords(1, MAX_Y), ADJACENT_CELLS_DICT[Coords(1, MAX_Y)])
                             ])
    def test_initialization(self, current_coord, expected_adjacent_cells):
        assert AdjacentCells(current_coord, MAX_X, MAX_Y).possible_adjacent_cells == expected_adjacent_cells

    @pytest.mark.parametrize("adjacent_cell1, adjacent_cell2, expected",
                             [
                                 (AdjacentCells(Coords(1, 1), MAX_X, MAX_Y), AdjacentCells(Coords(1, 1), MAX_X, MAX_Y),
                                  True),
                                 (AdjacentCells(Coords(1, 1), MAX_X, MAX_Y), AdjacentCells(Coords(2, 2), MAX_X, MAX_Y),
                                  False)
                             ])
    def test_equality(self, adjacent_cell1, adjacent_cell2, expected):
        assert (adjacent_cell1 == adjacent_cell2) == expected

    @pytest.mark.parametrize("adjacent_cell1, adjacent_cell2, expected",
                             [
                                 (AdjacentCells(Coords(1, 1), MAX_X, MAX_Y), AdjacentCells(Coords(1, 1), MAX_X, MAX_Y),
                                  False),
                                 (AdjacentCells(Coords(1, 1), MAX_X, MAX_Y), AdjacentCells(Coords(2, 2), MAX_X, MAX_Y),
                                  True)
                             ])
    def test_inequality(self, adjacent_cell1, adjacent_cell2, expected):
        assert (adjacent_cell1 != adjacent_cell2) == expected

    def test_hash(self):
        assert AdjacentCells(Coords(0, 0), MAX_X, MAX_Y).__hash__() == hash(
            tuple({6: Coords(x=1, y=0), 2: Coords(x=0, y=1), 3: Coords(x=1, y=1)}))
