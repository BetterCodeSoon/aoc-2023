def strip_list_items(input_list: [str]) -> [str]:
    if input_list is None:
        raise ValueError("The input list cannot be None!")
    return [item.strip() for item in input_list]


def remove_empty_strings(input_list: [str]) -> [str]:
    if input_list is None:
        raise ValueError("The input list cannot be None!")
    return [item for item in input_list if item.strip() != ""]


def is_single_char(delimiter: str):
    if delimiter is None:
        raise ValueError("String is None")
    if len(delimiter) <= 1:
        return True
    return False


def to_int(input_list: [str]) -> [int]:
    return [int(item) for item in input_list if item != ""]


def flat_int_list(value_list: [[str]]) -> [int]:
    return [int(value) for sublist in value_list for value in sublist if value != '']


def char_count(input_str: str) -> {str: int}:
    """
    Returns a dictionary with the number of occurrences for each char in the input string \n
    e.g.: "AAAAAAA" -> {'A': 7}
    """
    char_count_dict = {}
    for i in range(0, len(input_str)):
        char = input_str[i]
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    return char_count_dict
