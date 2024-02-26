from typing import List


class InputLine:

    def __init__(self, input_str: str, delimiter: str = "", strip_trailing_whitespaces: bool = True):
        if input_str is None:
            raise ValueError("The line string is None")

        self.line_str = input_str

        if not self._is_single_char(delimiter):
            raise ValueError(f"The length of '{delimiter}' is not 0 or 1")

        self.delimiter = delimiter
        self.strip_trailing_whitespaces = strip_trailing_whitespaces
        self.next_line_parts: List[InputLine] = []

        if delimiter != "" and delimiter in input_str:
            self._split_line_str(input_str)

    @staticmethod
    def _is_single_char(delimiter: str):
        if delimiter is None:
            raise ValueError("String is None")
        if len(delimiter) <= 1:
            return True
        return False

    def has_parts(self):
        if len(self.next_line_parts) > 0:
            return True
        return False

    def _split_line_str(self, line_str: str):
        parts = line_str.split(self.delimiter)

        if self.strip_trailing_whitespaces:
            parts = self._strip_list_items(parts)

        self.line_str = parts[0]
        self.next_line_parts = self._remove_empty_strings(parts[1:])

        if self.strip_trailing_whitespaces:
            self.line_str = self.line_str.strip()
            self.next_line_parts = self._strip_list_items(self.next_line_parts)

    @staticmethod
    def _strip_list_items(input_list: List):
        return [item.strip() for item in input_list]

    @staticmethod
    def _remove_empty_strings(input_list: List):
        return [item for item in input_list if item.strip() != ""]

    def __eq__(self, other):
        return (self.line_str == other.line_str
                and self.delimiter == other.delimiter
                and self.strip_trailing_whitespaces == other.strip_trailing_whitespaces
                and self.next_line_parts == other.next_line_parts)

    def __ne__(self, other):
        return not self.__eq__(other)
