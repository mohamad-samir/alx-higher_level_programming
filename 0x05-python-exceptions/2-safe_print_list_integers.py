#!/usr/bin/python3
"""function that prints the first x elements of a list and only integers

    Args:
        my_list: list to print
        x: number of elements to print

    Return:
        number of elements printed
"""


def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    element_printed = 0
    while x > 0:
        try:
            print("{:d}".format(my_list[idx]), end="")
            idx += 1
            x -= 1
        except TypeError:
            idx += 1
            x -= 1
        except ValueError:
            idx += 1
            x -= 1
        else:
            element_printed += 1

    print()

    return element_printed
