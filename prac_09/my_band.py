"""
CP1404/CP5632 Practical
Band class using association with Musicians
"""

class Band:
    """Represents a music band with multiple musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a readable description of the band and its musicians."""
        musician_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_string})"

    def add(self, musician):
        """Add a Musician object to the band's roster."""
        self.musicians.append(musician)

    def play(self):
        """Have each musician play their instrument and return all outputs as a string."""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)
