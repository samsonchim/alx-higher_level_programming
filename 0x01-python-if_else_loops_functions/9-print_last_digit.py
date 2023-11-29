def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit

# Test cases
print_last_digit(123)  # Output: 3
print_last_digit(-456)  # Output: 6
print_last_digit(0)  # Output: 0
