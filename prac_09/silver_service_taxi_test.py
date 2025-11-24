"""
CP1404/CP5632 Practical
SilverServiceTaxi class test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Luxury Limo", 200, 4)

    # Drive 0 km to show initial state
    taxi.drive(0)
    print(taxi)
    print(f"Total Ride Price: ${taxi.get_fare():.2f}")

    # Drive 18 km to calculate fare
    taxi.drive(20)
    print(taxi)
    print(f"Total Ride Price: ${taxi.get_fare():.2f}")


main()
