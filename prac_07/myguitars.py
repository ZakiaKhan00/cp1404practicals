"""
CP1404/CP5632 Practical - More Guitars
Reads and writes a list of Guitar objects to a CSV file.
"""

from guitar import Guitar

def main():
    """Read guitars from file, allow user to add more, sort, and save back."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    guitars += get_new_guitars()

    save_guitars(filename, guitars)
    print(f"\nAll guitars have been saved to {filename}.")


def load_guitars(filename):
    """Read guitars from the CSV file."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def get_new_guitars():
    """Ask user for new guitars and return them as a list of Guitar objects."""
    new_guitars = []
    print("\nEnter new guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        new_guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")
    return new_guitars

def display_guitars(guitars):
    """Display all guitars in a formatted list."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def save_guitars(filename, guitars):
    """Write all guitars back to the CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

if __name__ == "__main__":
    main()
