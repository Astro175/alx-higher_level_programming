#!/usr/bin/python3
combination_count = 0
for number in range(100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end= ", ")
