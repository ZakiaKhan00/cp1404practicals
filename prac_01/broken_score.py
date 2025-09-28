"""
Program to classify a score as invalid, bad, passable, or excellent.
Score must be between 0 and 100 inclusive; 90 or more is excellent; 50 or more is a pass; below 50 is bad.

Pseudocode:
get score
if score < 0 or score > 100
    print Invalid score
elif score >= 90
    print Excellent
elif score >= 50
    print Passable
else
    print Bad
"""

score = float(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

"""
Test Case
Enter your score: -5
Invalid score

Enter your score: 0
Bad

Enter your score: 49
Bad

Enter your score: 50
Passable

Enter your score: 80
Passable

Enter your score: 95
Excellent

Enter your score: 100
Excellent

Enter your score: 150
Invalid score
"""