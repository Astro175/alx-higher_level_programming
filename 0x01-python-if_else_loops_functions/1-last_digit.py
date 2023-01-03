#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the absolute value of number
last_digit = abs(number) % 10

# Print the last digit and additional text based on its value
print("Last digit of", number, "is", end="")
if number < 0:
    print("-", end="")
print(last_digit, end="")
if abs(number) % 10 > 5:
    print(" and is greater than 5")
elif abs(number) % 10 == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")

