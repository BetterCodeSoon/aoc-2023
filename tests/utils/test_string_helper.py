from src.utils.string_helper import *


class TestStringHelper:

    def test_strip_list_items(self):
        assert strip_list_items(["1", "", " 2", "  ", " 3 "]) == ["1", "", "2", "", "3"]

    def test_remove_empty_strings(self):
        assert remove_empty_strings(["1", "", " 2", "  ", " 3 "]) == ["1", " 2", " 3 "]

    def test_is_single_char(self):
        assert is_single_char("1") is True
        assert is_single_char("") is True
        assert is_single_char("23") is False
