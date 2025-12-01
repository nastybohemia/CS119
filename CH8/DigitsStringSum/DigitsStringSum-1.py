# A Sum of Digits in a String
# Author: Sofia Popova
# LACC CS119
# Task: A program that displayes the sum of a series of single-digit numbers with nothing separating them entered by a user.

# get input a number string
def get_input():
    user_input = input("Enter a series of single-digit numbers with no spaces: ")
    return user_input

# calculations
def calc_sum(numbers_str):
    total = 0
    for ch in numbers_str:
        if ch.isdigit():
            total += int(ch)
    return total

# display a formatted message for output 
def display(numbers_str, result):
    """Display a formatted message with the results."""
    print("\n----- RESULT -----")
    print(f"You entered: {numbers_str}")
    print(f"The sum of the digits is: {result}")
    print("-------------------\n")

# Call main
def main():
    numbers = get_input()
    result = calc_sum(numbers)
    display(numbers, result)
main()