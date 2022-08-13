import unittest
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def engine_needs_service(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def engine_doesnt_need_service(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())
