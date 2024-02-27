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
