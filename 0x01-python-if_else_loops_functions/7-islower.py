#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
