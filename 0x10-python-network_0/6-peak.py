#!/usr/bin/python3
"""Module that checks for the highest number"""

def find_peak(list_of_integers):
    """Function that take a list and returns
       the peak number of that list
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    mid = n // 2
    if list_of_integers[mid] >= list_of_integers[mid - 1] and \
       list_of_integers[mid] >= list_of_integers[mid + 1]:
           return list_of_integers[mid]
    if list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])
    return find_peak(list_of_integers[:mid])
