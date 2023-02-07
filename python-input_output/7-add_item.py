#!/usr/bin/python3
"""
    Module to load, add and save all arguments to a Python
    list in a file
"""

# to use argument on line command
import sys
# to test if file already exist
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
path = Path('./add_item.json')

# if file exist, append and not overwrite
if path.is_file():
    my_obj = load_from_json_file(filename)
    my_obj = my_obj + sys.argv[1:]
    save_to_json_file(my_obj, filename)
else:
    save_to_json_file(sys.argv[1:], filename)
