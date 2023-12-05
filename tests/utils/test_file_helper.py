import src.utils.file_helper as file_helper
from tests.conftest import testfile_path


def test_get_puzzle_input_path():
    day = 1
    filename = "day1_puzzle1_input.txt"
    expected_path = file_helper.PROJECT_ROOT / "resources" / f"day{day}" / filename
    assert expected_path == file_helper.get_puzzle_input_path(day, filename)


def test_read_file_lines(testfile_path):
    file_content = file_helper.read_file_lines(testfile_path)
    assert file_content == ['123\n', '\n', '456\n', '789']
