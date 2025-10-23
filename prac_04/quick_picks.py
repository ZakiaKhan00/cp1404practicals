"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random

NUMBERS_PER_PICK = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    """Get the number of quick pick from the user they wish to generate."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks <= 0:
        print("Please enter a number greater than zero.")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = quick_pick_generator()
        print(" ".join(f"{number:2}" for number in quick_pick))

def quick_pick_generator():
        quick_pick = []
        for j in range(NUMBERS_PER_PICK):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        return quick_pick
main()
