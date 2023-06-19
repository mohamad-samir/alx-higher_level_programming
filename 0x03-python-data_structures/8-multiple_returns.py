#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Args:
        sentence: a string argument

    Returns:
        a tuple with the length of a string and its first character
    """

    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return length, first

