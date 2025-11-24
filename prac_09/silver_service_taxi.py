"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A fancy taxi with a flagfall and increased price per km based on fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi, plus fanciness multiplier."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the fare including the flagfall."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string like Taxi but with flagfall included."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"