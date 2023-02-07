#!/usr/bin/python3
"""
  Module that converts argument to a python list,
  and save them into a file
"""


import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    for item in sys.argv[1:]:
        items.append(item)

    save_to_json_file(items, filename)
