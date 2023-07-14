#!/usr/bin/python3
"""Load, add, save"""
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    # Load the existing list from the file, if it exists
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    my_list = []

# Add the arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
