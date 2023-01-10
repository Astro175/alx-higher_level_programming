#!/usr/bin/python3
if idx < 0 or idx >= len(my_list):
    return my_list
return my_list[:idx] + my_list[idx+1:]
