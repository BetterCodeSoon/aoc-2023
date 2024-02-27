from src.utils.string_helper import remove_empty_strings, strip_list_items


class TestStringHelper:

    def test_strip_list_items(self):
        assert strip_list_items(["1", "", " 2", "  ", " 3 "]) == ["1", "", "2", "", "3"]

    def test_remove_empty_strings(self):
        assert remove_empty_strings(["1", "", " 2", "  ", " 3 "]) == ["1", " 2", " 3 "]
