import pytest
import src.aoc2.aoc2 as aoc2
import src.utils.file_helper as file_helper


def example_test_cases():
    file_path = file_helper.puzzle_testcases_path(2, 1)

    # toDo turn input from e.g.: 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    # into --> game_id = 1
    #          first_set = {'red': 4, 'blue': 3, 'green': 0}
    #          second_set = {'red': 1, 'blue': 6, 'green': 2}
    #          third_set = {'red': 0, 'blue': 0, 'green': 2}
