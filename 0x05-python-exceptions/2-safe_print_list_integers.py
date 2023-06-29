#!/usr/bin/python3
"""function that prints the first x elements of a list and only integers

    Args:
        my_list: list to print
        x: number of elements to print

    Return:
        number of elements printed
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return count
