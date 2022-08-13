import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = date.fromisoformat("2019-02-02")
        newBattery = SpindlerBattery(last_service_date)
        self.assertTrue(newBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = date.fromisoformat("2021-02-02")
        newBattery = SpindlerBattery(last_service_date)
        self.assertFalse(newBattery.needs_service())