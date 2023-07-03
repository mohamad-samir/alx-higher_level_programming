#!/usr/bin/python3
"""This module contains a function that splits text by specified delimiters."""


def text_indentation(text):
    """Prints text separated by deliiters, line by line.

    Args:
        text (str): Text to print.

    Raises:
        TypeError: If text given is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        if char in [".", "?", ":"]:
            result += char + "\n\n"
        else:
            result += char

    print(result)
