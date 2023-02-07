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
n = len(sys.argv)
path = Path('./add_item.json')

# if file exist, append and not overwrite
if path.is_file():
    my_obj = load_from_json_file(filename)
    if n != 1:
        for i in range(1, n):
            my_obj.append(str(sys.argv[i]))
else:
    my_obj = []

save_to_json_file(my_obj, filename)

load_from_json_file(filename)
