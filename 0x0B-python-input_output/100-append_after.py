#!/usr/bin/python3
"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """
        Inserts a line of text to a file, after each line containing
        a specific string.

    Args:
        filename (str, optional): Path to the file. Defaults to "".
        search_string (str, optional): String to search for. Defaults to "".
        new_string (str, optional): String to be appended. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, mode="w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
