import unittest
from simulator import Simulator
from algorithms.scheduling import Scheduling

class testAlgorithmsBaseFunctions(unittest.TestCase):
    """Tests base functions in Scheduling."""
    
    _requirements = [-5, 15, 40, 65, 20, -35]
    _reqs_no_pf = [15, 40, 65, 20]

    def setUp(self):
        self.sched = Scheduling()
        self.init_pos = 0

    def test_startup(self):
        """Check startup initializes the simulation lists."""
        pos = self.sched.startup(self._requirements, self.init_pos)
        self.assertEqual(pos, 35)
        self.assertEqual(self.sched.page_faults, [0, 5, 35])
        self.assertEqual(self.sched.requirements, [15, 40, 65, 20])

    def test_count_movements(self):
        """Check correct amount of movements is calculated"""
        pos = self.sched.startup(self._requirements, self.init_pos)
        movements = self.sched.count_movements(self.sched.requirements, pos)
        self.assertEqual(movements, 115)

    def test_divide_list(self):
        """Check divide list returns two lists in correct order."""
        self.sched.startup(self._requirements, self.init_pos)
        greater, lower = self.sched.divide_list(self.sched.requirements, self.init_pos, False)
        self.assertEqual(greater, [15, 40, 65, 20])
        self.assertEqual(lower, [])

    def test_get_end_dir(self):
        """Check final direction is correct"""
        dir = self.sched.get_end_dir(self._reqs_no_pf, self.init_pos, True)
        self.assertEqual(dir, False)

    def test_get_last_req(self):
        """Check last requirement is returned correctly"""
        last_req = self.sched.get_last_req(self._reqs_no_pf, self.init_pos)
        self.assertEqual(last_req, 20)

class testStandaloneFunctions(unittest.TestCase):
    

    def setUp(self):
         self.simulator = Simulator()

    def test_random_list_should_create_x_amount_reqs(self):
        """Check length of requirements"""
        self.simulator.random_list(33)
        self.assertEqual(len(self.simulator.requirements),33)

    def test_random_list_should_return_list(self):
        self.assertIsInstance(self.simulator.requirements, list)

class testSimulator(unittest.TestCase):
    """Tests default algorithms under various significant circumstances."""

    def setUp(self):
         self.simulator = Simulator()
         self.simulator.init_pos = 0
         self.simulator.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]

    def test_FCFS(self):
        base_results = (([[0, 5, 35, 400], [15, 40, 65, 20, 90, 100]], 960, True), 'FCFS')
        self.assertEqual(self.simulator.execute_algorithm('FCFS'), base_results)
        
        self.simulator.init_pos=self.simulator.max_tracks
        base_results = (([[511, 5, 35, 400], [15, 40, 65, 20, 90, 100]], 1461, True), 'FCFS')
        self.assertEqual(self.simulator.execute_algorithm('FCFS'), base_results)

    def test_SSTF(self):
        base_results = (([[0, 5, 35, 400], [100, 90, 65, 40, 20, 15]], 785, False), 'SSTF')
        self.assertEqual(self.simulator.execute_algorithm('SSTF'), base_results)

        self.simulator.init_pos=self.simulator.max_tracks
        base_results = (([[511, 5, 35, 400], [100, 90, 65, 40, 20, 15]], 1286, False), 'SSTF')
        self.assertEqual(self.simulator.execute_algorithm('SSTF'), base_results)
       

    def test_SCAN(self):
        base_results = (([[0, 5, 35, 400], [self.simulator.max_tracks, 100, 90, 65, 40, 20, 15]], 1007, False), 'SCAN')
        self.assertEqual(self.simulator.execute_algorithm('SCAN'), base_results)

        self.simulator.init_pos=self.simulator.max_tracks
        base_results = (([[self.simulator.max_tracks, 5, 35, 400], [self.simulator.max_tracks, 100, 90, 65, 40, 20, 15]], 1508, False), 'SCAN')
        self.assertEqual(self.simulator.execute_algorithm('SCAN'), base_results)

    def test_CSCAN(self):
        base_results = (([[0, 5, 35, 400], [self.simulator.max_tracks], [0, 15, 20, 40, 65, 90, 100]], 611, True), 'CSCAN')
        self.assertEqual(self.simulator.execute_algorithm('CSCAN'), base_results)

        self.simulator.init_pos=self.simulator.max_tracks
        base_results = (([[511, 5, 35, 400], [self.simulator.max_tracks], [0, 15, 20, 40, 65, 90, 100]], 1112, True), 'CSCAN')
        self.assertEqual(self.simulator.execute_algorithm('CSCAN'), base_results)

    def test_LOOK(self):
        base_results = (([[0, 5, 35, 400], [100, 90, 65, 40, 20, 15]], 485, False), 'LOOK')
        self.assertEqual(self.simulator.execute_algorithm('LOOK'), base_results)

    def test_CLOOK(self):
        base_results = (([[0, 5, 35, 400], [], [15, 20, 40, 65, 90, 100]], 485, True), 'CLOOK')
        self.assertEqual(self.simulator.execute_algorithm('CLOOK'), base_results)


class testSimulatorNoPageFaults(unittest.TestCase):
    """Tests default algorithms without page faults."""

    def setUp(self):
         self.simulator = Simulator()
         self.simulator.init_pos = 0
         self.simulator.requirements = [5, 15, 40, 65, 20, 35, 400, 90, 100]

    def test_FCFS(self):
        base_results = (([[], [0, 5, 15, 40, 65, 20, 35, 400, 90, 100]], 810, True), 'FCFS')
        self.assertEqual(self.simulator.execute_algorithm('FCFS'), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511, 5, 15, 40, 65, 20, 35, 400, 90, 100]], 1311, True), 'FCFS')
        self.assertEqual(self.simulator.execute_algorithm('FCFS'), base_results)

    def test_SSTF(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400]], 400, True), 'SSTF')
        self.assertEqual(self.simulator.execute_algorithm('SSTF'), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511, 400, 100, 90, 65, 40, 35, 20, 15, 5]], 506, False), 'SSTF')
        self.assertEqual(self.simulator.execute_algorithm('SSTF'), base_results)

    def test_SCAN(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400]], 400, True), 'SCAN')
        self.assertEqual(self.simulator.execute_algorithm('SCAN'), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511, 400, 100, 90, 65, 40, 35, 20, 15, 5]], 506, False), 'SCAN')
        self.assertEqual(self.simulator.execute_algorithm('SCAN'), base_results)

    def test_CSCAN(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400], []], 400, True), 'CSCAN')
        self.assertEqual(self.simulator.execute_algorithm('CSCAN'), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400]], 400, True), 'CSCAN')
        self.assertEqual(self.simulator.execute_algorithm('CSCAN'), base_results)

    def test_LOOK(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400]], 400, True), 'LOOK')
        self.assertEqual(self.simulator.execute_algorithm('LOOK'), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511, 400, 100, 90, 65, 40, 35, 20, 15, 5]], 506, False), 'LOOK')
        self.assertEqual(self.simulator.execute_algorithm('LOOK'), base_results)

    def test_CLOOK(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400], []], 400, True), 'CLOOK')
        self.assertEqual(self.simulator.execute_algorithm('CLOOK'), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [self.simulator.max_tracks], [5, 15, 20, 35, 40, 65, 90, 100, 400]], 395, True), 'CLOOK')
        self.assertEqual(self.simulator.execute_algorithm('CLOOK'), base_results)


class TestSimulatorFalseDirection(unittest.TestCase):

    def setUp(self):
        self.simulator = Simulator()
        self.simulator.init_pos = 0
        self.simulator.direction = False
        self.simulator.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]

    # def test_dir_post_CSCAN(self):
    #     self.simulator.execute_algorithm('CSCAN')
    #     self.assertEqual(self.simulator.algorithm.last_dir, self.simulator.direction)

    # def test_dir_post_CLOOK(self):
    #     self.simulator.execute_algorithm('CLOOK')
    #     self.assertEqual(self.simulator.algorithm.last_dir, self.simulator.direction)
