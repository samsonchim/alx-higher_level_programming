#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert the character to uppercase using ASCII manipulation
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(char), end='')
    print()

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
