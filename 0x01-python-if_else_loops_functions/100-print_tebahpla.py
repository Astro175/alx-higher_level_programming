#!/usr/bin/python3
# Create a list of lowercase ASCII characters in reverse order
characters = [chr(i) for i in range(ord('z'), ord('a')-1, -2)]

# Repeat the list twice
characters = characters * 2

# Join the characters into a single string using the `format` function
string = '{}'.format(*characters)

# Reverse the string using string slicing
string = string[::-1]

# Print the string, suppressing the new line at the end
print(string, end='')
