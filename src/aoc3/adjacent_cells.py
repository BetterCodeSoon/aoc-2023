from src.aoc3 import Coords


# noinspection SpellCheckingInspection
class AdjacentCells:

    def __init__(self, current_coords: Coords, max_x: int, max_y: int):
        if max_x < 2 or max_y < 2:
            raise ValueError(f"The minimum required dimensions are 3x3. Max_x: {max_x} x Max_y: {max_y} is too low!\n")

        """
         The dictory is build in Numpad Style:

         7     8        9
         4 Current Cell 6
         1     2        3

         e.g. cells below current cell have the keys: 1, 2, 3         
         """
        self.possible_adjacent_cells: {int: Coords} = {}
        self.possible_adjacent_cells.update(self._adjacent_left(current_coords))
        self.possible_adjacent_cells.update(self._adjacent_right(current_coords, max_x))
        self.possible_adjacent_cells.update(self._adjacent_on_top(current_coords, max_x))
        self.possible_adjacent_cells.update(self._adjacent_below(current_coords, max_x, max_y))

    @staticmethod
    def _adjacent_on_top(current_coords: Coords, max_x: int) -> {int: Coords}:
        adjacent_cells_on_top: {int: Coords} = {}

        # Already on the top border of the schematics --> so no row on top
        if current_coords.y == 0:
            return adjacent_cells_on_top

        top_y = current_coords.y - 1

        # Current on the left border
        if current_coords.x == 0:
            adjacent_cells_on_top[8] = Coords(0, top_y)
            adjacent_cells_on_top[9] = Coords(1, top_y)
            return adjacent_cells_on_top

        # Current on the right border
        if current_coords.x == max_x:
            adjacent_cells_on_top[8] = Coords(max_x, top_y)
            adjacent_cells_on_top[7] = Coords(max_x - 1, top_y)
            return adjacent_cells_on_top

        # Current somewhere between borders
        adjacent_cells_on_top[7] = Coords(current_coords.x - 1, top_y)
        adjacent_cells_on_top[8] = Coords(current_coords.x, top_y)
        adjacent_cells_on_top[9] = Coords(current_coords.x + 1, top_y)
        return adjacent_cells_on_top

    @staticmethod
    def _adjacent_below(current_coords: Coords, max_x: int, max_y: int) -> {int: Coords}:
        adjacent_cells_below: {int: Coords} = {}

        # Already on the bottom --> so there is no row further down
        if current_coords.y == max_y:
            return adjacent_cells_below

        bellow_y = current_coords.y + 1

        # Current on the left border
        if current_coords.x == 0:
            adjacent_cells_below[2] = Coords(0, bellow_y)
            adjacent_cells_below[3] = Coords(1, bellow_y)
            return adjacent_cells_below

        # Current on the right border
        if current_coords.x == max_x:
            adjacent_cells_below[2] = Coords(max_x, bellow_y)
            adjacent_cells_below[1] = Coords(max_x - 1, bellow_y)
            return adjacent_cells_below

        # Current somewhere between borders
        adjacent_cells_below[1] = Coords(current_coords.x - 1, bellow_y)
        adjacent_cells_below[2] = Coords(current_coords.x, bellow_y)
        adjacent_cells_below[3] = Coords(current_coords.x + 1, bellow_y)
        return adjacent_cells_below

    @staticmethod
    def _adjacent_left(current_coords: Coords) -> {int: Coords}:
        adjacent_cell_left: {int: Coords} = {}

        # Current on the left border
        if current_coords.x == 0:
            return adjacent_cell_left

        adjacent_cell_left[4] = Coords(current_coords.x - 1, current_coords.y)
        return adjacent_cell_left

    @staticmethod
    def _adjacent_right(current_coords: Coords, max_x: int) -> {int: Coords}:
        adjacent_cell_right: {int: Coords} = {}

        # Current on the right border
        if current_coords.x == max_x:
            return adjacent_cell_right

        adjacent_cell_right[6] = Coords(current_coords.x + 1, current_coords.y)
        return adjacent_cell_right

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return self.possible_adjacent_cells == other.possible_adjacent_cells

    def __ne__(self, other):
        return not self.__eq__(other)
