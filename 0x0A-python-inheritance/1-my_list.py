#!/usr/bin/python3
"""
  Module that inherits a list and prints the element
"""


class Mylist(list):
    """
    My list class that inherits list and prints its attributes
    """
    def print_sorted(self):
        """
           Method that prints sorted list
        """
        print(sorted(self))
