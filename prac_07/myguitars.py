"""
CP1404/CP5632 Practical - More Guitars
Reads and writes a list of Guitar objects to a CSV file.
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from file, allow user to add more, sort, and save back."""
    guitars = load_guitars()
    print("My guitars!")

    if guitars:
        display_guitars(guitars)
    else:
        print("No guitars found in the file.")

    name = input("\nName: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")

    guitars.sort()

    print("\nSorted guitars:")
    display_guitars(guitars)

    save_guitars(guitars)
    print(f"\nAll guitars have been saved to {FILENAME}.")


def load_guitars():
    """Read guitars from the CSV file."""
    guitars = []
    try:
        with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
            for line in in_file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, year, cost = parts[0], int(parts[1]), float(parts[2])
                    guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"Warning: {FILENAME} not found, starting with an empty list.")
    return guitars


def save_guitars(guitars):
    """Write all guitars back to the CSV file."""
    with open(FILENAME, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    """Display all guitars neatly."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


main()
