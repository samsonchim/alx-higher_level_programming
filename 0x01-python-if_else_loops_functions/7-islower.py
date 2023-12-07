#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of the character is within the range of lowercase letters
    return 97 <= ord(c) <= 122

# Test cases
print(islower('a'))  # Output: True
print(islower('A'))  # Output: False
print(islower('z'))  # Output: True
print(islower('Z'))  # Output: False
print(islower('1'))  # Output: False
