#!/usr/bin/python3
"""Load, add, save"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Load the existing list from the file, if it exists
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    my_list = []
except json.JSONDecodeError:
    print("Invalid JSON format in the file.")
    sys.exit(1)

# Add the arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
try:
    save_to_json_file(my_list, filename)
except Exception as e:
    print(f"Error saving the list to the file: {e}")
    sys.exit(1)
