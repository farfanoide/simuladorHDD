import unittest
from simulator import Simulator
class testSimulator(unittest.TestCase):
    """tests default functions"""

    def setUp(self):
        self.reqs = Simulator()
        self.reqs.requirements = [80, 44, 230, 128, 511, 90, 56, 6, 444, 211]
        self.reqs.add_random_pf(4)

    def test_random_list_should_return_list(self):
        self.assertIsInstance(self.reqs.requirements, list)

    def test_random_list_should_create_x_amount_reqs(self):
        self.reqs.random_list(33)
        self.assertEqual(len(self.reqs.requirements),33)

    def test_momentum_should_return_amount_of_movements(self):
        self.assertEqual(self.reqs.momentum(self.reqs.requirements, self.reqs.init_pos), 2053)

    def test_add_random_pf_should_add_aprox_x_negative_numbers(self):

        def count_pfs(reqs):
            count = 0
            for req in reqs:
                if req < 0:
                    count += 1
            return count
                    
        self.assertLessEqual(count_pfs(self.reqs.requirements),4)

    # def test_fifo_returns_direction():
        


