from parking_spot import ParkingSpot

class ParkingLevel:
    def __init__(self, level_number, total_spots, spot_size):
        self.level_number = level_number
        self.total_spots = total_spots
        self.spot_size = spot_size  # Dictionary to track spots by vehicle type
        self.spots = [ParkingSpot(i, spot_size) for i in range(1, total_spots + 1)]

    def get_available_spot(self, vehicle_type):
        # Look for available spot for the given vehicle type
        for spot in self.spots:
            if not spot.occupied and (spot.vehicle_type == vehicle_type or spot.vehicle_type is None):
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.get_available_spot(vehicle.vehicle_type)
        if spot:
            spot.occupied = True
            spot.vehicle_type = vehicle.vehicle_type
            return spot
        return None

    def unpark_vehicle(self, spot_number):
        for spot in self.spots:
            if spot.spot_number == spot_number:
                spot.occupied = False
                spot.vehicle_type = None
                return spot
        return None

    def get_parking_status(self):
        available = sum(1 for spot in self.spots if not spot.occupied)
        return available
