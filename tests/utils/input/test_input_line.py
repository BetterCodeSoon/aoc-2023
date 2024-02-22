import pytest

from utils.input.input_line import InputLine


class TestInputLine:

    @pytest.mark.parametrize("input_str, expected_line, expected_exist, expected_values",
                             [("something| b1, b2", "something", True, ["b1", "b2"])])
    def test_input_line_initialization(self, input_str, expected_line, expected_exist, expected_values):
        input_line = InputLine(input_str)
        assert input_line.line_str
        assert input_line.has_expected_values is expected_exist
        assert input_line.expected_values_list == expected_values

    @pytest.mark.parametrize("input_line1, input_line2, expected",
                             [(InputLine("bla| b1, b2"), InputLine("bla| b1, b2"), True),
                              (InputLine("bla| b1, b2"), InputLine("bla"), False),
                              (InputLine("bla| b1, b2"), InputLine("bla| "), False),
                              (InputLine("bla| b1, b2"), InputLine("bla| x1"), False)])
    def test_equality(self, input_line1, input_line2, expected):
        assert (input_line1 == input_line2) is expected
