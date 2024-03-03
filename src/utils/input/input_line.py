from utils.string_helper import strip_list_items, is_single_char


class InputLine:

    def __init__(self, input_str: str, delimiter: str = "", strip_trailing_whitespaces: bool = True):
        if input_str is None:
            raise ValueError("The line string is None")

        self.line_str = input_str

        if not is_single_char(delimiter):
            raise ValueError(f"The length of '{delimiter}' is not 0 or 1")

        self.delimiter = delimiter
        self.strip_trailing_whitespaces = strip_trailing_whitespaces
        self.next_line_part: str = ""

        if delimiter != "" and delimiter in input_str:
            self._split_line_str(input_str)

    def has_parts(self):
        if len(self.next_line_part) > 0:
            return True
        return False

    def _split_line_str(self, line_str: str):
        parts = line_str.split(self.delimiter)

        if self.strip_trailing_whitespaces:
            parts = strip_list_items(parts)

        self.line_str = parts[0]
        self.next_line_part = parts[1:][0]

        if self.strip_trailing_whitespaces:
            self.line_str = self.line_str.strip()
            self.next_line_part = self.next_line_part.strip()

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return (self.line_str == other.line_str
                and self.delimiter == other.delimiter
                and self.strip_trailing_whitespaces == other.strip_trailing_whitespaces
                and self.next_line_part == other.next_line_part)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.line_str, self.next_line_part, self.delimiter, self.strip_trailing_whitespaces))
