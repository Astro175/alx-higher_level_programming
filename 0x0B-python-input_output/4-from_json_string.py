#!/usr/bin/python3
"""
   Module that returns a python structure,
   from a JSON string
"""


import json


def from_json_string(my_str):
    """function that returns python structure"""
    return json.loads(my_str)
