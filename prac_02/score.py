"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Program to determine score status"""
    user_score = float(input("Enter score: "))
    print(determine_score_status(user_score))

    random_score = random.randint(0,100)
    print(f"Random score is: {random_score}")
    print(determine_score_status(random_score))

def determine_score_status(score):
    """Determine status of the score"""
    if score < 0 or score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")

main()