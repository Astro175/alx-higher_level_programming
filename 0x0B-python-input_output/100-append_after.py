#!/usr/bin/python3
"""
  Module that searches a file for a string,
  and adds a new string
"""

def append_after(filename="", search_string="", new_string=""):
    """
       function that searches and adds a new_string
    """
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string + "\n")
    with open(filename, "w") as w:
        w.writelines(lines)
