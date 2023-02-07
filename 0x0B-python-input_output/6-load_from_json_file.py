#!/usr/bin/python3
"""
   Module that converts a json file to python object
"""


import json


def load_from_json_file(filename):
    """
       function that converts a json file to python object
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
