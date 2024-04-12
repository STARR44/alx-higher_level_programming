#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            temp = chr(ord(char) - 32)
        else: temp = char
        print("{}" .format(temp), end="")
    print('')
