from pathlib import Path

CURRENT_FILE = Path(__file__)
PROJECT_ROOT = CURRENT_FILE.parent.parent.parent


def path_for_day(day):
    return PROJECT_ROOT / "resources" / f"day{day}"


def puzzle_filename(day, puzzle_nr):
    return f"day{day}_puzzle{puzzle_nr}_input.txt"


def puzzle_input_path(day, puzzle_nr):
    """
    Naming convention for the files containing the puzzle inputs: \n
        resources \n
        ├── day{day} \n
        │   ├─ day{day}_puzzle{puzzle_nr}_input.txt \n

    example: day1_puzzle1_input.txt
    """
    return path_for_day(day) / puzzle_filename(day, puzzle_nr)


def puzzle_testcases_filename(day):
    return f"day{day}_testcases.txt"


def puzzle_testcases_path(day):
    """
    Naming convention for the files containing the puzzle inputs: \n
        resources \n
        ├── day{day} \n
        │   ├─ day{day}_testcases.txt \n

    example: day1_testcases.txt
    """
    return path_for_day(day) / puzzle_testcases_filename(day)


def read_file_lines(filepath):
    with open(filepath, "r") as file:
        return file.readlines()


def read_expected_values(filepath, delimiter) -> {str: str}:
    return {line.split(delimiter)[0]: line.split(delimiter)[1].strip() for line in read_file_lines(filepath)}


def read_test_values_tuple_list(filepath, delimiter) -> [(str, str)]:
    file_lines = read_file_lines(filepath)
    return [(line.split(delimiter)[0], line.split(delimiter)[1].strip()) for line in file_lines]
