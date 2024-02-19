from typing import List

from aoc2.bag import Bag
from aoc2.cube_container import CubeContainer


class ElfGame:

    game_id: int
    game_sets: [CubeContainer, CubeContainer, CubeContainer]

    def __init__(self, game_id: int, game_sets: List[CubeContainer]):
        if game_id is None or game_id <= 0:
            raise Exception(f"Game ID:{game_id} is invalid. It needs to be a positive Integer > 0")

        if any(game_set is None for game_set in game_sets):
            raise ValueError("Invalid game sets. At least one of the sets is not initialized.")

        if len(game_sets) != 3:
            raise Exception(f"The list of game sets does not contain exactly three sets. Its size is {len(game_sets)}")

        self.game_id = game_id
        self.game_sets = game_sets

    def possible_game(self, bag: Bag):
        # look in the bag remove the colored cubes for each game set
        # the game is ONLY possible if there are 0 or more cubes left in the bag
        if any(not bag.reveal_cubes_possible(game_set) for game_set in self.game_sets):
            return False
        return True
