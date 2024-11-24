import unittest
from time import sleep
from parking_system import ParkingSystem, Vehicle


class TestParkingSystem(unittest.TestCase):

    def setUp(self):
        # Setup for each test: create a parking system with two levels
        levels = {1: 5, 2: 6}  # Level 1 has 5 spots, Level 2 has 6 spots
        spot_size_map = {1: 'SUV', 2: 'Sedan'}  # Level 1 is for SUVs, Level 2 is for Sedans
        self.parking_system = ParkingSystem(levels, spot_size_map)

    def test_vehicle_initialization(self):
        # Test vehicle initialization
        vehicle = Vehicle("ABC123", "SUV")
        self.assertEqual(vehicle.license_plate, "ABC123")
        self.assertEqual(vehicle.vehicle_type, "SUV")
        self.assertEqual(str(vehicle), "SUV (ABC123)")

    def test_parking_ticket_creation(self):
        # Test creating a parking ticket
        vehicle = Vehicle("XYZ456", "Sedan")
        ticket = self.parking_system.park_vehicle("XYZ456", "Sedan")

        self.assertIsNotNone(ticket)
        self.assertEqual(ticket.vehicle.license_plate, "XYZ456")
        self.assertEqual(ticket.vehicle.vehicle_type, "Sedan")
        self.assertEqual(ticket.level, 2)  # As per spot_size_map, Level 2 is for Sedans
        self.assertIsNone(ticket.exit_time)  # Exit time should be None when parked

    def test_parking_and_unparking(self):
        # Test parking and unparking a vehicle
        vehicle = Vehicle("ABC123", "SUV")
        ticket = self.parking_system.park_vehicle("ABC123", "SUV")

        # Check parking status
        self.parking_system.show_parking_status()
        self.assertEqual(self.parking_system.parking_lot.levels[1].get_parking_status(), 4)  # 1 spot occupied

        # Simulate vehicle leaving after some time
        sleep(1)  # Simulate a short parking duration
        fee = self.parking_system.unpark_vehicle(ticket)

        self.assertGreater(fee, 0)  # Fee should be greater than 0

    def test_parking_status(self):
        # Test parking status reporting
        vehicle1 = Vehicle("ABC123", "SUV")
        ticket1 = self.parking_system.park_vehicle("ABC123", "SUV")

        vehicle2 = Vehicle("XYZ456", "Sedan")
        ticket2 = self.parking_system.park_vehicle("XYZ456", "Sedan")

        self.parking_system.show_parking_status()
        # After parking 2 vehicles, Level 1 should have 4 spots left for SUVs, Level 2 should have 5 spots left for Sedans


if __name__ == '__main__':
    unittest.main()
