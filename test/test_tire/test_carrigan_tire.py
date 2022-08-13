import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_needs_service(self):
        tire = CarriganTire([0, 0, 0, 1])
        self.assertTrue(tire.needs_service())

    def test_tire_does_not_need_service(self):
        tire = CarriganTire()
        self.assertFalse(tire.needs_service())
