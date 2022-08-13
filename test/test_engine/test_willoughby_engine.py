import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def engine_needs_service(self):
        current_milage = 70000
        last_service_milage = 0
        engine = WilloughbyEngine(last_service_milage, current_milage)
        self.assertTrue(engine.needs_service())

    def engine_doesnt_need_service(self):
        current_milage = 0
        last_service_milage = 0
        engine = WilloughbyEngine(last_service_milage, current_milage)
        self.assertFalse(engine.needs_service())
