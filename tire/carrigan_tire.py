from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensors=[0, 0, 0, 0]) -> None:
        self.sensors = sensors

    def needs_service(self):
        for tire in self.sensors:
            if tire >= 0.9:
                return True
        return False
