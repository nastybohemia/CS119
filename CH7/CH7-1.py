# The two exercises are related. Build your program in a modular way, then you need to only change the function that builds the list.

# Task: A modular program for the number analysis
# Author: Sofia Popova
# LACC CS119

# libraries
import random

# get input values (1 - 20)
def get_numbers():
    """Builds a list of the numbers 1–20."""
    numbers = [] #list
    for i in range(1, 21):
        numbers.append(i)
    return numbers

# display the results in a formatted message
def display_results(numbers):
    print("Number Analysis Results")
    print("-" * 30)
    print("List of Numbers: ", numbers)
    print("Lowest Value:   ", min(numbers))
    print("Highest Value:  ", max(numbers))
    print("Total:          ", sum(numbers))
    print("Average:        ", sum(numbers) / len(numbers))
    print("-" * 30)
    
# generate 20 random numbers between 1 & 100.
def build_list_random():
    numbers2 = [] #list
    for i in range(20):
        numbers2.append(random.randint(1, 100)) #random number generator
    return numbers2

# display main to invoke these two
def main():
    nums = get_numbers()
    display_results(nums)

# Ask user if they want to continue to part (b)
    cont = input("Continue to random number analysis? (y/n): ")

    if cont.lower() == "y":
        # PART (b) — random list
        random_nums = build_list_random()
        print("20 Random Numbers: ", random_nums)
        display_results(random_nums)
    else:
        print("Program ended.")

main()
