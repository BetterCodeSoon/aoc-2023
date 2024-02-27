import pytest

from src.utils.input.input_line import InputLine


class TestInputLine:

    @staticmethod
    def create_l(input_str: str) -> InputLine:
        return InputLine(input_str, "|")

    @pytest.mark.parametrize("input_str, expected_line, expected_has_parts, expected_parts",
                             [("something| ", "something", False, ""),
                              ("something", "something", False, ""),
                              ("something| b1, b2", "something", True, "b1, b2"),
                              ("something| b1 , b2   ", "something", True, "b1 , b2"),
                              ("something| b1", "something", True, "b1")])
    def test_input_line_initialization(self, input_str, expected_line, expected_has_parts, expected_parts):
        input_line = InputLine(input_str, "|", True)
        assert input_line.line_str == expected_line
        assert input_line.has_parts() is expected_has_parts
        assert input_line.next_line_parts == expected_parts

    @pytest.mark.parametrize("input_line1, input_line2, expected",
                             [(create_l("bla| b1, b2"), create_l("bla| b1, b2"), True),
                              (create_l("bla| b1, b2"), create_l("bla"), False),
                              (create_l("bla| b1, b2"), create_l("bla| "), False),
                              (create_l("bla| b1, b2"), create_l("bla| x1"), False)])
    def test_equality(self, input_line1, input_line2, expected):
        assert (input_line1 == input_line2) is expected

    @pytest.mark.parametrize("input_line1, input_line2, expected",
                             [(create_l("bla| b1, b2"), create_l("bla| b1, b2"), False),
                              (create_l("bla| b1, b2"), create_l("bla"), True),
                              (create_l("bla| b1, b2"), create_l("bla| "), True),
                              (create_l("bla| b1, b2"), create_l("bla| x1"), True)])
    def test_inequality(self, input_line1, input_line2, expected):
        assert (input_line1 != input_line2) is expected
