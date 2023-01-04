#!/usr/bin/python3
def uppercase(string):
    result = ""

    for c in string:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            result = chr(ord(c) - 32)
        else:
            result += c

        print("{}".format(result) end = "")
