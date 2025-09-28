"""
CP1404/CP5632 - Practical

Pseudocode:
MENU = C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
print MENU

get choice
while choice != Q
    if choice == C
        get celsius
        calculate fahrenheit = (celsius × 9 / 5) + 32
        print fahrenheit
    elif choice == F
        get fahrenheit
        calculate celsius = (fahrenheit - 32) × 5 / 9
        print celsius
    else
        print invalid option
    print MENU
    get choice

print Thank You
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9.0 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")