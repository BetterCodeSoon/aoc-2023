import pytest

from src.aoc3.cell import Cell
from src.aoc3.schematic_number import SchematicNumber
from tests.aoc3.test_cell import create_cell


def cell_list(number_str: str) -> [Cell]:
    return [create_cell(0, y, digit) for y, digit in enumerate(number_str)]


class TestSchematicNumber:

    @pytest.mark.parametrize("cells, expected_value", [
        (cell_list("1"), 1),
        (cell_list("123"), 123)
    ])
    def test_initialization(self, cells, expected_value):
        assert SchematicNumber(cells).value == expected_value

    @pytest.mark.parametrize("cell1, cell2, expected", [
        (create_cell(1, 1, "."), create_cell(1, 1, "."), True),
        (create_cell(1, 1, "."), create_cell(2, 2, "."), False)
    ])
    def test_equality(self, cell1, cell2, expected):
        assert (cell1 == cell2) == expected

    @pytest.mark.parametrize("cell1, cell2, expected", [
        (create_cell(1, 1, "."), create_cell(1, 1, "."), False),
        (create_cell(1, 1, "."), create_cell(2, 2, "."), True)
    ])
    def test_inequality(self, cell1, cell2, expected):
        assert (cell1 != cell2) == expected

    def test_hash(self):
        value = 1234
        cells = cell_list(str(value))
        number = SchematicNumber(cells)
        assert number.__hash__() == hash((tuple(cells), value))
