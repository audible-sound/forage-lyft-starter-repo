import unittest
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_needs_service(self):
        tire = OctoprimeTire([1, 1, 1, 1])
        self.assertTrue(tire.needs_service())

    def test_tire_does_not_need_service(self):
        tire = OctoprimeTire()
        self.assertFalse(tire.needs_service())
