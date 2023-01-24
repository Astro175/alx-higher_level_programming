#!/usr/bin/python3
"""Class that calculates area of square"""

class Square:
    """Creating attributes"""
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            return self.__size ** 2

