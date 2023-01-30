#!/usr/bin/python3
"""Module that creates a rectangle"""


class Rectangle:
    """Class for Rectangle Blueprint"""
    def __init__(self, width=0, height=0):
        """init width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height
    
    @height.setter
    def heigth(self, value):
        """sets the heigth attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
