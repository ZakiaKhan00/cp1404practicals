"""
CP1404/CP5632 Practical
Wimbledon data processing
Estimate: 30 minutes
Actual:   39 minutes
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    """Program to read data file and print details about Wimbledon information."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

def process_records(records):
    """Create dictionary of champions and set of countries from Wimbledon records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Display champions with their win counts and list of winning countries."""
    print("Wimbledon Champions: ")
    max_champion_len = max(len(champion) for champion in champion_to_count)
    for name, count in sorted(champion_to_count.items()):
        print(f"{name:{max_champion_len}} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

def load_records(filename):
    """Load data from csv file into a list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records

main()