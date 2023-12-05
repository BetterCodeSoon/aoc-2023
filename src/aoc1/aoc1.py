import re
import src.utils.file_helper as file_helper

WRITTEN_DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                  "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def find_written_digits(input_string):
    # written_digits_found = {}
    # for key in WRITTEN_DIGITS:
    #     result = input_string.find(key)
    #     if result != -1:
    #         written_digits_found[key] = input_string.find(key)

    return {key: input_string.find(key) for key in WRITTEN_DIGITS if key in input_string}


def find_first_written_digit(written_digits_found_dict):
    """
    :param written_digits_found_dict: the lower the value of a key the earlier it appears in the input string
    :return: key with the lowest value
    """
    return min(written_digits_found_dict, key=written_digits_found_dict.get)


def find_last_written_digit(written_digits_found_dict):
    """
    :param written_digits_found_dict: the higher the value of a key the earlier it appears in the input string
    :return: key with the highest value
    """
    return max(written_digits_found_dict, key=written_digits_found_dict.get)


def replace_written_digits(input_string):

    # cover case that there is no written digit
    replaced_digits_str = input_string

    digits_found = find_written_digits(input_string)
    if len(digits_found) != 0:
        first_written_digit = find_first_written_digit(digits_found)
        replaced_digits_str = input_string.replace(first_written_digit, WRITTEN_DIGITS[first_written_digit])

        # check if there is another digit
        digits_found = find_written_digits(replaced_digits_str)
        if len(digits_found) != 0:
            last_written_digit = find_last_written_digit(find_written_digits(replaced_digits_str))
            replaced_digits_str = replaced_digits_str.replace(last_written_digit, WRITTEN_DIGITS[last_written_digit])

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

    ###debug_dict = {}

    calibration_values = []
    for line in file_lines:
        # replace the first and last occurrence of a written digit
        replaced_written_digits = replace_written_digits(line)
        # find the first and last occurrence of a digit and collect its int value
        calibration_values.append(int(find_calibration_value(replaced_written_digits)))
        ###debug_dict[line] = int(find_calibration_value(replaced_written_digits))

    ###s = sum(debug_dict.values())
    print(f"The total calibration sum = {sum(calibration_values)}\n")
