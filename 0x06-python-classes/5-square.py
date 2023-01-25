#!/usr/bin/python3
"""defines a module"""


class Square:
    """defines a sqaure class"""
    def __init__(self, size=0):
        """initialises the size variable"""
        self.size = size

    @property
    def size(self):
        """returns private attibute"""
        return self.__size

    @size.setter
    def size(self, value):
        """checks the value passed"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """sets the area"""
        return self.__size ** 2

    def my_print(self):
        """prints the size"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
