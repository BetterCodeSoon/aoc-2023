from src import TYPE_TESTCASE
from src.utils.input.input_file import InputFile
from src.utils.input.input_line import InputLine
from src.utils.string_helper import strip_list_items


class TestcaseInputFile(InputFile):

    def __init__(self, day: int, file_number: int, comment_marker: str = '~', values_delimiter: str = '|',
                 value_separator: str = ','):
        super().__init__(TYPE_TESTCASE, day, file_number, comment_marker)

        self.testcase_input_lines: [InputLine] = [InputLine(line, values_delimiter) for line in self.file_lines]

        next_line_parts = [input_line.next_line_part for input_line in self.testcase_input_lines]
        self.testcase_expected_values: [[str]] = self._separate_values(next_line_parts, value_separator)

    @staticmethod
    def _separate_values(next_line_parts: [str], value_separator: str) -> [[str]]:
        return [strip_list_items(value) for value in [part.split(value_separator) for part in next_line_parts]]

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return (super().__eq__(other)
                and self.testcase_input_lines == other.testcase_input_lines
                and self.testcase_expected_values == other.testcase_expected_values)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.file_path, self.file_lines, self.testcase_input_lines, self.testcase_expected_values))
