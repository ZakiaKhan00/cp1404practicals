"""
CP1404/CP5632 Practical
Unreliable_Car class
"""

from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """Car that sometimes does not drive."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive only if random number is less than reliability."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven