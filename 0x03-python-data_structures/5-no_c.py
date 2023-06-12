#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to removes all characters c and C from a string
# -----------------------------------------------------------

def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c not in "Cc":
            new_string += c
    return new_string
