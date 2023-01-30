#!/usr/bin/python3
"""Module that creates Rectangle"""


class Rectangle:
    """Creates a blueprint for rectangles"""

    def __init__(self, width=0, height=0):
        """init height and width attribute"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """returns the height attribute"""
        return self.__height
    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """returns the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__width = value
    
    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
