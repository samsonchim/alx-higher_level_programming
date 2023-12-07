#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert the character to uppercase using ASCII manipulation
            result += "{}".format(chr(ord(char) - 32))
        else:
            result += "{}".format(char)

    print(result)

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
