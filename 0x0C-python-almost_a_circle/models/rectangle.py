#!/usr/bin/python3
"""Module that creates a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class that creates a rectangle model"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width of the class"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the class"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method that returns the area of a rectangle"""
        return self.height * self.width
    def display(self):
        """Method that prints the rectangle with a #"""
        for _ in range(self.height):
            print("#" * self.width)
