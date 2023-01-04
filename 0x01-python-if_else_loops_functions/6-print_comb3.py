#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print("{}, ".format(f"{i:01d}{j:01d}"), end="")
print("89")
