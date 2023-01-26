#!/usr/bin/python3
"""defines a module"""
import math


class MagicClass:
    """magic class"""
    def __init__(self, radius):
        """init for radius"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """def for area"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """de3f for circumference"""
        return 2 * math.pi * self.__radius
