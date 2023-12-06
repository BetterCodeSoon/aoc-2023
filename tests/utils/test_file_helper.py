import pytest

import src.utils.file_helper as file_helper
from tests.conftest import testfile_content
from tests.conftest import testfile_path


# @pytest.mark.parametrize(
#     ("expected_key", "expected_val"),
#     [
#         ("1abc2", "12"),
#         ("pqr3stu8vwx", "38"),
#         ("a1b2c3d4e5f", "15"),
#         ("treb7uchet", "77")
#     ])
class TestFileHelper:
    def test_get_puzzle_filename(self):
        n = 1
        expected = f"day{n}_puzzle{n}_input.txt"
        assert expected == file_helper.get_puzzle_filename(n, n)

    def test_get_puzzle_input_path(self):
        day = 1
        puzzle_nr = 1
        filename = file_helper.get_puzzle_filename(day, puzzle_nr)
        expected_path = file_helper.PROJECT_ROOT / "resources" / f"day{day}" / filename
        assert expected_path == file_helper.get_puzzle_input_path(day, puzzle_nr)

    def test_read_file_lines(self, testfile_path, testfile_content):
        file_content = file_helper.read_file_lines(testfile_path)
        assert file_content == testfile_content

    @pytest.mark.skip("yet to be implemented")
    def test_read_expected_values(self, testfile_path):
        pass
