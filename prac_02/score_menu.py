"""
CP1404/CP5632 - Practical
Program for score menu
"""

import random

MENU = """ (G)et a valid score \n (P)rint result \n (S)how stars \n (Q)uit"""

def main():
    # score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(f"Result: {determine_score_status(score)}")
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")

def get_valid_score():
    score = float(input("Enter score between 0 to 100: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Enter score between 0 to 100: "))
    return (score)

def determine_score_status(score):
    if score >= 90:
        return"Excellent"
    elif score >= 50:
        return"Passable"
    else:
        return"Bad"

def show_stars(score):
    print('*' * int(score))


main()