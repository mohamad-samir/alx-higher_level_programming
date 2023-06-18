#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position

    Args:
        my_list: a list
        idx: the index of item to replace
        element: item to be substituted

    Returns:
        the edited list
    """

    # Check for negative and out of range index
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
