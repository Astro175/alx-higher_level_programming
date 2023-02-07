#!/usr/bin/python3
"""Module that opens and reads a file"""


def read_file(filename=""):
    """function that reads file"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
