from pathlib import Path

CURRENT_FILE = Path(__file__)
PROJECT_ROOT = CURRENT_FILE.parent.parent


def get_puzzle_input_path(day, filename):
    return PROJECT_ROOT / "resources" / f"day{day}" / filename


def read_file_lines(filepath):

    with open(filepath, "r") as file:
        return file.readlines()
