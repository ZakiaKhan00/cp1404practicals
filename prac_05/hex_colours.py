"""
CP1404/CP5632 Practical
Hexadecimal colour codes lookup
"""

# Constant dictionary of colour names and hexadecimal codes
COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aqua": "#00ffff",
                "beige": "#f5f5dc", "coral": "#ff7f50","crimson": "#dc143c","gold": "#ffd700",
                "lavender": "#e6e6fa", "navy": "#000080", "salmon": "#fa8072"}

colour_name = input("Enter colour name: ").lower()
while colour_name !="":
    if colour_name in COLOUR_CODES:
        print(f"{colour_name.capitalize()} - {COLOUR_CODES[colour_name]}")
    else:
        print("Invalid colour name.")
    colour_name = input("Enter colour name: ").lower()

