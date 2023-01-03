#!/usr/bin/python3
alphabet = ''
for i in range(ord('a'), ord('z')+1):
    if chr(i) not in ['q', 'e']:
        alphabet += chr(i)
print("{}".format(alphabet), end='')
