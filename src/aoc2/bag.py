from src.aoc2.cube_container import CubeContainer


class Bag(CubeContainer):

    def reveal_cubes_possible(self, game_set: CubeContainer) -> bool:
        if game_set is None:
            raise Exception("Cannot analyse a game set that is not initialized.")
        if self.red < game_set.red:
            return False
        if self.green < game_set.green:
            return False
        if self.blue < game_set.blue:
            return False
        return True
