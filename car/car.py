from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, Engine, Battery) -> None:
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False
