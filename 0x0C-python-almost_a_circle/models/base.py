#!/usr/bin/python3
"""Module that creates a base class"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init method for arguments"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
