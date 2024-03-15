import pytest

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

    @pytest.mark.parametrize("hand_str, expected", [
        ("AAAAAAA", {'A': 7}),
        ("11A2B", {'1': 2, 'A': 1, '2': 1, 'B': 1})
    ])
    def test_char_count(self, hand_str, expected):
        assert char_count(hand_str) == expected
