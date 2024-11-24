from datetime import datetime

class ParkingTicket:
    def __init__(self, vehicle, level, spot_number):
        self.vehicle = vehicle
        self.level = level
        self.spot_number = spot_number
        self.entry_time = datetime.now()
        self.exit_time = None

    def calculate_parking_fee(self):
        if not self.exit_time:
            return 0  # Can't calculate if the vehicle hasn't exited yet

        # Example fee: $2 per hour
        duration = (self.exit_time - self.entry_time).total_seconds() / 3600
        return round(duration * 2, 2)  # $2 per hour

    def __repr__(self):
        return f"Ticket for {self.vehicle} at Level {self.level}, Spot {self.spot_number}, Entry: {self.entry_time}"
