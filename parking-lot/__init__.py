from time import sleep

from parking_system import ParkingSystem
from datetime import time

if __name__ == "__main__":
    levels = {1: 5, 2: 6}  # Level 1 has 5 spots, Level 2 has 6 spots
    spot_size_map = {1: 'SUV', 2: 'Sedan'}  # Level 1 is for SUVs, Level 2 is for Sedans

    parking_system = ParkingSystem(levels, spot_size_map)

    # Park some vehicles
    ticket1 = parking_system.park_vehicle("ABC123", "SUV")
    ticket2 = parking_system.park_vehicle("XYZ456", "Sedan")
    ticket3 = parking_system.park_vehicle("LMN789", "Sedan")

    parking_system.show_parking_status()

    # Simulate vehicle leaving (after some time)
    sleep(2)
    parking_system.unpark_vehicle(ticket1)
    parking_system.show_parking_status()

    # Park another vehicle
    ticket4 = parking_system.park_vehicle("DEF101", "SUV")
    parking_system.show_parking_status()

    # Unpark remaining vehicles
    parking_system.unpark_vehicle(ticket2)
    parking_system.unpark_vehicle(ticket3)
    parking_system.unpark_vehicle(ticket4)