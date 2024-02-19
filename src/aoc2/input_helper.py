from aoc2.cube_container import CubeContainer

R = "red"
G = "green"
B = "blue"


def read_game_sets_list(input_string, delimiter="; ") -> [CubeContainer]:
    """
    e.g. for "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" the function returns
     --> [CubeContainer(4, 0, 3), CubeContainer(1, 2, 6), CubeContainer(0, 2, 0)]
    :param input_string:
    :param delimiter:
    :return: List of CubeContainers
    """
    game_set_strings = input_string.split(delimiter)
    return [read_game_set(game_set_str) for game_set_str in game_set_strings]


def read_game_set(game_set_str, delimiter=", ") -> CubeContainer:
    color_count_dict = {R: 0, G: 0, B: 0}

    # e.g. game_set_str = '3 blue, 4 red'
    # split into ['3 blue', '4 red']
    color_strings = game_set_str.split(delimiter)

    for colour_str in color_strings:
        count, color_name = read_color(colour_str)
        color_count_dict[color_name] += count

    return CubeContainer(color_count_dict[R], color_count_dict[G], color_count_dict[B])


def read_color(color_str, delimiter=" ") -> (int, str):
    # e.g. '3 blue' --> (3, 'blue')
    count, color_name = color_str.split(delimiter)
    return int(count), str(color_name)
