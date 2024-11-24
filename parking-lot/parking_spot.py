class ParkingSpot:
    def __init__(self, spot_number, vehicle_type=None):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type  # None means the spot is free
        self.occupied = False

    def __repr__(self):
        return f"Spot {self.spot_number} ({self.vehicle_type if self.vehicle_type else 'Empty'})"
