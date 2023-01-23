#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    element_printed = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            element_printed += 1
        except IndexError:
            break
    print()
    return element_printed
