#!/usr/bin/python3

def max_integer(numbers_list):
    """
    Args:
        my_list: a list

    Returns:
        the biggest integer in list or none if list is empty
    """

    if not numbers_list:
        return None

    max_value = numbers_list[0]
    for number in numbers_list:
        if number > max_value:
            max_value = number
    
    return max_value
