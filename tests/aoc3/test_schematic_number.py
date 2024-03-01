import pytest

from src.aoc3.cell import Cell
from src.aoc3.schematic_number import SchematicNumber
from tests.aoc3.test_cell import create_cell


def number_cell_list(number_str: str) -> [Cell]:
    return [create_cell(x, 0, digit) for x, digit in enumerate(number_str)]


class TestSchematicNumber:

    @pytest.mark.parametrize("cells, expected_value", [
        (number_cell_list("1"), 1),
        (number_cell_list("123"), 123)
    ])
    def test_initialization(self, cells, expected_value):
        assert SchematicNumber(cells).value == expected_value

    def test_add_cell(self):
        expected_cells = number_cell_list("12")
        cell1 = expected_cells[0]
        cell2 = expected_cells[1]
        number = SchematicNumber([cell1])
        number.add_cell(cell2)
        assert number.cells == expected_cells

    @pytest.mark.parametrize("expected_cells, coord_x, expected_value, expected_error", [
        (number_cell_list("12"), 0, 12, None),
        (number_cell_list("12"), 1, 12, ValueError)
    ])
    def test_add_cell(self, expected_cells, coord_x, expected_value, expected_error):
        cell1: Cell = expected_cells[0]
        cell2: Cell = expected_cells[1]
        cell2.coords.x += coord_x
        number = SchematicNumber([cell1])
        if expected_error is None:
            assert number.add_cell(cell2) is None
            assert number.cells == expected_cells
            assert number.value == expected_value
        else:
            with pytest.raises(expected_error):
                number.add_cell(cell2)

    @pytest.mark.parametrize("y, element, number_row_y, expected", [
        (2, '5', 2, None),  # Test case for same row and digit
        (3, '7', 2, ValueError),  # Test case for different row
        (2, '#', 2, ValueError)  # Test case for non-digit element
    ])
    def test_validate_cell(self, y, element, number_row_y, expected):
        number = SchematicNumber([create_cell(0, 2, "1")])
        cell = create_cell(1, y, element)

        if expected is None:
            assert number._validate_cell(cell) is expected
        else:
            with pytest.raises(expected):
                number._validate_cell(cell)

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
        row_y = 0
        value = 1234
        cells = number_cell_list(str(value))
        number = SchematicNumber(cells)
        assert number.__hash__() == hash((row_y, tuple(cells), value))
