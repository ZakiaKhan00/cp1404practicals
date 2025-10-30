"""
CP1404/CP5632 Practical- Guitar class
Estimate = 30 mins
Actual = 25 mins
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string describing the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get age of guitar in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar age is greater than 50"""
        return self.get_age() >= VINTAGE_AGE