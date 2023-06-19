#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific location
      without modifying the original

    Args:
        my_list: a list
        idx: the index of item to replace
        element: item to be substituted

    Returns:
        the edited list copy
    """

    temp_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return temp_list
    temp_list[idx] = element
    return temp_list
