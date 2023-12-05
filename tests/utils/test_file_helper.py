import src.utils.file_helper as file_helper
from tests.conftest import testfile_path


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

    def test_read_file_lines(self, testfile_path):
        file_content = file_helper.read_file_lines(testfile_path)
        assert file_content == ['123\n', '\n', '456\n', '789']
