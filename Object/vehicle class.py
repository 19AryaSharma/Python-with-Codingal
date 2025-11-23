class vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = vehicle(240, 18)
print("Model Max Speed is",modelx.max_speed)
print("model Mileage is",modelx.mileage)