class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def __repr__(self):
        return f"{self.vehicle_type} ({self.license_plate})"
