#!/usr/bin/python3
"""defines a module"""


class Square:
    """Defines a class that creates squares"""
    def __init__(self, size=0):
        "initialises an object"""
        self.size = size

    @property
    def size(self):
        """returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size value"""
        if not ininstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """defines the area"""
        return self.__size ** 2
