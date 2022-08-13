import unittest
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_milage = 50000
        last_service_milage = 0
        engine = CapuletEngine(last_service_milage, current_milage)
        self.assertTrue(engine.needs_service())

    def test_engine_doesnt_need_service(self):
        current_milage = 0
        last_service_milage = 0
        engine = CapuletEngine(last_service_milage, current_milage)
        self.assertFalse(engine.needs_service())
