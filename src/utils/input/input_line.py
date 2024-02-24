class InputLine:
    expected_values_list: [str]
    has_expected_values: bool = False
    line_str: str

    def __init__(self, input_str: str, delimiter: str = '| ', value_separator: str = ', ',
                 strip_trailing_spaces: bool = True):
        """
        e.g. for a line in a File: "something| b1, b2" the class would look like this: \n\n

        :param input_str: "something" in the above example
        :param delimiter: "| " in the above example aka what separates input string from expected values
        :param value_separator: what separates "b1, b2" aka ", "
        :param strip_trailing_spaces: IF True then "b1 , b2   " is turned to ["b1", "b2"] otherwise ["b1 ", "b2   "]
        """

        if input_str is None:
            raise Exception(f"input string is None")

        expected_str = None
        if delimiter in input_str:
            self.line_str, expected_str = input_str.split(delimiter)
            self.line_str = self.line_str.replace(delimiter, "")  # in case expected_str is empty
        else:
            self.line_str = input_str

        if expected_str is not None and len(expected_str) > 0:
            expected_values = expected_str.split(value_separator)
            if strip_trailing_spaces:
                expected_values = [value.strip() for value in expected_values]
            self.expected_values_list = expected_values
            self.has_expected_values = True
        else:
            self.expected_values_list = []

    def __eq__(self, other):
        return (self.line_str == other.line_str
                and self.expected_values_list == other.expected_values_list
                and self.has_expected_values == other.has_expected_values)

    def __ne__(self, other):
        return not self.__eq__(other)
