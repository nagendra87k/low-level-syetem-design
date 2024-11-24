from parking_lot import ParkingLot
from vehicle import Vehicle

class ParkingSystem:
    def __init__(self, levels, spot_size_map):
        self.parking_lot = ParkingLot(levels, spot_size_map)

    def park_vehicle(self, license_plate, vehicle_type):
        vehicle = Vehicle(license_plate, vehicle_type)
        ticket = self.parking_lot.park_vehicle(vehicle)
        if ticket:
            print(f"Vehicle {vehicle} parked at Level {ticket.level}, Spot {ticket.spot_number}")
        return ticket

    def unpark_vehicle(self, ticket):
        fee = self.parking_lot.unpark_vehicle(ticket)
        print(f"Parking fee for vehicle {ticket.vehicle}: ${fee}")

    def show_parking_status(self):
        status = self.parking_lot.get_parking_status()
        print("Parking Status:")
        for level_num, level_status in status.items():
            print(f"Level {level_num}: {level_status['available_spots']} available out of {level_status['total_spots']} spots")
