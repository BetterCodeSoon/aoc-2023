from src.aoc2.elf_game import ElfGame
from src.aoc2.cube_container import CubeContainer, R, G, B


def read_game_sets_list(input_string, delimiter="; ") -> [CubeContainer]:
    """
    e.g. for "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" the function returns  \n\n
     --> [CubeContainer(4, 0, 3), CubeContainer(1, 2, 6), CubeContainer(0, 2, 0)] \n
    """
    game_set_strings = input_string.split(delimiter)
    return [read_game_set(game_set_str) for game_set_str in game_set_strings]


def read_game_set(game_set_str, delimiter=", ") -> CubeContainer:
    """
     e.g. game_set_str = '3 blue, 4 red'
     split into ['3 blue', '4 red'] and is returned as:
     --> CubeContainer(4, 0, 3)
    """
    color_count_dict = {R: 0, G: 0, B: 0}

    color_strings = game_set_str.split(delimiter)

    for colour_str in color_strings:
        count, color_name = read_color(colour_str)
        color_count_dict[color_name] += count

    return CubeContainer(color_count_dict[R], color_count_dict[G], color_count_dict[B])


def read_color(color_str, delimiter=" ") -> (int, str):
    """
    e.g. '3 blue' --> (3, 'blue')
    """
    count, color_name = color_str.split(delimiter)
    return int(count), str(color_name)


def read_game_id(game_str, delimiter=" ") -> int:
    """
    e.g. "Game 3" --> 3
    """
    temp, game_id = game_str.split(delimiter)
    return int(game_id)


def str_to_elf_game(elf_game_str: str) -> ElfGame:
    """
    e.g. Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # --> ElfGame(1, ... )
    """
    game_id_values_list = elf_game_str.split(": ")

    game_id = read_game_id(game_id_values_list[0])
    game_sets = read_game_sets_list(game_id_values_list[1])

    return ElfGame(game_id, game_sets)
