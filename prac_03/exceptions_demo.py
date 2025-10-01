"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# A valueError occurs when the program tries to convert a string that is not a valid integer.eg.seven (it's not a valid integer)
2. When will a ZeroDivisionError occur?
#A ZerDivisionError occurs when a denominator is entered as 0 (it can't be divided by zero)
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by checking that the denominator is not zero BEFORE dividing, we avoid a ZeroDivisionError entirely.
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    #avoid dividing by zero
    if denominator != 0:
        #handle division when denominator is valid
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!") #displays that dividing by zero is not allowed
except ValueError:
    print("Numerator and denominator must be valid numbers!") #handles invalid integer
finally:
    print("Finished.") #always run

"""
Test Case:
-----Valid-----

Enter the numerator: 10
Enter the denominator: 2
5.0
Finished.

----ValueError----

Enter the numerator: seven
Numerator and denominator must be valid numbers!
Finished.

Enter the numerator: 8
Enter the denominator: 2.4
Numerator and denominator must be valid numbers!
Finished.

----ZeroDivisionError----
Enter the numerator: 10
Enter the denominator: 0
Cannot divide by zero!
Finished
"""