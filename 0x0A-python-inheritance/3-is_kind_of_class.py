#!/usr/bin/python3
"""
   Module that checks if an object is an instance,
   or inherited from a sub-class
"""


def is_kind_of_class(obj, a_class):
    """checks for object instance compared to a class"""
    return (isinstance(obj, a_class))
