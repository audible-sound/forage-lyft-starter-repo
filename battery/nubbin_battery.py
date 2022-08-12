from datetime import datetime
from battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date + 4)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False