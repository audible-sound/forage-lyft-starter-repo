import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = date.fromisoformat("2000-02-02")
        newBattery = NubbinBattery(last_service_date)
        self.assertTrue(newBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = date.fromisoformat("2022-02-02")
        newBattery = NubbinBattery(last_service_date)
        self.assertFalse(newBattery.needs_service())
