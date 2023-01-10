#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for item in my_list:
        result.append(item % 2 == 0)
        return result
