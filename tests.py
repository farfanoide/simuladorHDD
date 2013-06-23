import unittest
from simulator import Simulator
class testSimulator(unittest.TestCase):
    """tests default functions"""

    def setUp(self):
        self.reqs = Simulator()

    def test_random_list_should_return_list(self):
        self.assertIsInstance(self.reqs.requirements, list)
