#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    element_printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            element_printed += 1
        print()
        except IndexError:
            pass
    return element_printed
