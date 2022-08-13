from car.car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory():
    @staticmethod
    def create_calliope(last_service_date, last_service_milage, current_milage, tire_sensors):
        car_engine = CapuletEngine(last_service_milage, current_milage)
        car_battery = SpindlerBattery(last_service_date)
        car_tire = CarriganTire(tire_sensors)
        return Car(car_engine, car_battery, car_tire)

    @staticmethod
    def create_glissade(last_service_date, last_service_milage, current_milage, tire_sensors):
        car_engine = WilloughbyEngine(last_service_milage, current_milage)
        car_battery = SpindlerBattery(last_service_date)
        car_tire = CarriganTire(tire_sensors)
        return Car(car_engine, car_battery, car_tire)

    @staticmethod
    def create_palindrome(last_service_date, warning_light_on, tire_sensors):
        car_engine = SternmanEngine(warning_light_on)
        car_battery = SpindlerBattery(last_service_date)
        car_tire = CarriganTire(tire_sensors)
        return Car(car_engine, car_battery, car_tire)

    @staticmethod
    def create_rorschach(last_service_date, last_service_milage, current_milage, tire_sensors):
        car_engine = WilloughbyEngine(last_service_milage, current_milage)
        car_battery = NubbinBattery(last_service_date)
        car_tire = OctoprimeTire(tire_sensors)
        return Car(car_engine, car_battery, car_tire)

    @staticmethod
    def create_thovex(last_service_date, last_service_milage, current_milage, tire_sensors):
        car_engine = CapuletEngine(last_service_milage, current_milage)
        car_battery = NubbinBattery(last_service_date)
        car_tire = OctoprimeTire(tire_sensors)
        return Car(car_engine, car_battery, tire_sensors)
