from datetime import datetime

from parking_level import ParkingLevel
from parking_ticket import ParkingTicket

class ParkingLot:
    def __init__(self, levels, spot_size_map):
        self.levels = {level_num: ParkingLevel(level_num, spot_count, spot_size_map.get(level_num, 'Sedan'))
                       for level_num, spot_count in levels.items()}

    def park_vehicle(self, vehicle):
        for level in self.levels.values():
            spot = level.park_vehicle(vehicle)
            if spot:
                ticket = ParkingTicket(vehicle, level.level_number, spot.spot_number)
                return ticket
        print(f"No parking spots available for vehicle {vehicle}")
        return None

    def unpark_vehicle(self, ticket):
        level = self.levels[ticket.level]
        spot = level.unpark_vehicle(ticket.spot_number)
        ticket.exit_time = datetime.now()
        return ticket.calculate_parking_fee()

    def get_parking_status(self):
        status = {}
        for level_num, level in self.levels.items():
            status[level_num] = {
                "total_spots": level.total_spots,
                "available_spots": level.get_parking_status()
            }
        return status
