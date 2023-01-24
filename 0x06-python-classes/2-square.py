#!/usr/bin/python3
"""Class that creates a private attribute and uses try to check if it is an int"""

class Square:
    """private attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

