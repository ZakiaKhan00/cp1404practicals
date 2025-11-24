"""
CP1404/CP5632 Practical
UnreliableCar class tests
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Test some UnreliableCars."""

    # cars with high and low reliability
    good_car = UnreliableCar("Junky", 100, 90)
    bad_car = UnreliableCar("Trusty", 100, 9)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:16} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:16} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)

main()