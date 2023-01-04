#!/usr/bin/python3
def islower(c):
    if c == c.lower():
        return "{} => lower".format(c)
    else:
        return "{} => upper".format(c)
