import re
import src.utils.file_helper as file_helper


def replace_written_digits(input_string):
    replaced_digits_str = "placeholder until function is written"
    return replaced_digits_str


def find_calibration_value(input_string):
    """
    Finds the first and last digit in an input string.
    For strings with only one digit that digit is treated as appearing twice.
    :param input_string: example "bla1bla2"
    :return: example "12"
    """
    # remove all non digit characters from the input string
    digit_string = re.sub(r"\D", "", input_string)

    # covering the case that there is no digit
    first_digit = "0"

    # find first digit
    match = re.search(r"\d", digit_string)
    if match is not None:
        first_digit = match.group(0)

    # covering the case that there is no second digit
    second_digit = first_digit

    # reverse digit string with splicing and find last digit
    match = re.search(r"\d", digit_string[::-1])
    if match is not None:
        second_digit = match.group(0)

    return first_digit + second_digit


if __name__ == '__main__':
    puzzle_path = file_helper.get_puzzle_input_path(1, 1)
    file_lines = file_helper.read_file_lines(puzzle_path)

    calibration_values = []
    for line in file_lines:
        calibration_values.append(int(find_calibration_value(line)))

    print(f"The total calibration sum = {sum(calibration_values)}\n")
