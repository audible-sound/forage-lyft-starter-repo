from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, Engine, Battery, Tire) -> None:
        self.engine = Engine
        self.battery = Battery
        self.tire = Tire

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False
