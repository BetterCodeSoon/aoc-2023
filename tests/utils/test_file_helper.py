import pytest

import src.utils.file_helper as file_helper
import conftest  # this works despite pycharm marking the statement as unused


class TestFileHelper:

    def test_puzzle_testcases_filename(self):
        n = 1
        expected = f"day{n}_testcases{n}.txt"
        assert expected == file_helper.puzzle_testcases_filename(n, n)

    def test_puzzle_testcase_path(self):
        n = 1
        filename = file_helper.puzzle_testcases_filename(n, n)
        expected = file_helper.PROJECT_ROOT / "resources" / f"day{n}" / filename
        result = file_helper.puzzle_testcases_path(n, n)
        assert result == expected

    def test_puzzle_filename(self):
        n = 1
        expected = f"day{n}_puzzle{n}_input.txt"
        assert expected == file_helper.puzzle_filename(n, n)

    def test_puzzle_input_path(self):
        day = 1
        puzzle_nr = 1
        filename = file_helper.puzzle_filename(day, puzzle_nr)
        expected_path = file_helper.PROJECT_ROOT / "resources" / f"day{day}" / filename
        assert expected_path == file_helper.puzzle_input_path(day, puzzle_nr)

    def test_read_file_lines(self, testfile1_path, file_helper_testfile1_content_lines):
        file_content = file_helper.read_file_lines(testfile1_path)
        assert file_content == file_helper_testfile1_content_lines

    def test_read_expected_values(self, testfile1_path, testfile1_delimiter, testfile1_dict):
        result_dict = file_helper.read_expected_values(testfile1_path, testfile1_delimiter)
        assert result_dict == testfile1_dict

    def test_read_test_values_tuple_list(self, testfile1_path, testfile1_delimiter, testfile1_tuple_list):
        result_list = file_helper.read_test_values_tuple_list(testfile1_path, testfile1_delimiter)
        assert result_list == testfile1_tuple_list
