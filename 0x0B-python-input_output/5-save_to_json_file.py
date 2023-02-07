#!/usr/bin/python3
"""
   Module that writes into a file, a json object
"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes json into a file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
