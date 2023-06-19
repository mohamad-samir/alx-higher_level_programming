#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        a tuple with 2 integers:
    """

    a1, a2 = (tuple_a + (0, 0))[:2]
    b1, b2 = (tuple_b + (0, 0))[:2]
    return a1 + b1, a2 + b2
