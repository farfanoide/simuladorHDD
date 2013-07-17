import unittest
from simulator import Simulator

class testStandaloneFunctions(unittest.TestCase):
    

    def setUp(self):
         self.simulator = Simulator()

    def test_random_list_should_create_x_amount_reqs(self):
         self.simulator.random_list(33)
         self.assertEqual(len(self.simulator.requirements),33)

    def test_random_list_should_return_list(self):
        self.assertIsInstance(self.simulator.requirements, list)

class testSimulator(unittest.TestCase):
    """tests default functions"""

    def setUp(self):
         self.simulator = Simulator()
         self.simulator.init_pos = 0
         self.simulator.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]

    def test_FCFS_shoud_return(self):
        base_results = (([[0, 5, 35, 400], [15, 40, 65, 20, 90, 100]], 960, True), 'FCFS')
        self.assertEqual(self.simulator.executeFCFS(), base_results)
        
        self.simulator.init_pos=self.simulator.max_tracks
        base_results = (([[511, 5, 35, 400], [15, 40, 65, 20, 90, 100]], 1461, True), 'FCFS')
        self.assertEqual(self.simulator.executeFCFS(), base_results)

    def test_SSTF_shoud_return(self):
        base_results = (([[0, 5, 35, 400], [100, 90, 65, 40, 20, 15]], 785, False), 'SSTF')
        self.assertEqual(self.simulator.executeSSTF(), base_results)

        self.simulator.init_pos=self.simulator.max_tracks
        base_results = (([[511, 5, 35, 400], [100, 90, 65, 40, 20, 15]], 1286, False), 'SSTF')
        self.assertEqual(self.simulator.executeSSTF(), base_results)
       

    def test_SCAN_shoud_return(self):
        base_results = (([[0, 5, 35, 400], [self.simulator.max_tracks, 100, 90, 65, 40, 20, 15]], 1007, False), 'SCAN')
        self.assertEqual(self.simulator.executeSCAN(), base_results)

        self.simulator.init_pos=self.simulator.max_tracks
        base_results = (([[self.simulator.max_tracks, 5, 35, 400], [self.simulator.max_tracks, 100, 90, 65, 40, 20, 15]], 1508, False), 'SCAN')
        self.assertEqual(self.simulator.executeSCAN(), base_results)

    def test_CSCAN_shoud_return(self):
        base_results = (([[0, 5, 35, 400], [self.simulator.max_tracks], [0, 15, 20, 40, 65, 90, 100]], 611, True), 'CSCAN')
        self.assertEqual(self.simulator.executeCSCAN(), base_results)

        self.simulator.init_pos=self.simulator.max_tracks
        base_results = (([[511, 5, 35, 400], [self.simulator.max_tracks], [0, 15, 20, 40, 65, 90, 100]], 1112, True), 'CSCAN')
        self.assertEqual(self.simulator.executeCSCAN(), base_results)

    def test_LOOK_shoud_return(self):
        base_results = (([[0, 5, 35, 400], [100, 90, 65, 40, 20, 15]], 485, False), 'LOOK')
        self.assertEqual(self.simulator.executeLOOK(), base_results)

    def test_CLOOK_shoud_return(self):
        base_results = (([[0, 5, 35, 400], [], [15, 20, 40, 65, 90, 100]], 485, True), 'CLOOK')
        self.assertEqual(self.simulator.executeCLOOK(), base_results)


class testSimulatorNoPageFaults(unittest.TestCase):
    """tests default functions"""

    def setUp(self):
         self.simulator = Simulator()
         self.simulator.init_pos = 0
         self.simulator.requirements = [5, 15, 40, 65, 20, 35, 400, 90, 100]

    def test_FCFS_shoud_return(self):
        base_results = (([[], [0, 5, 15, 40, 65, 20, 35, 400, 90, 100]], 810, True), 'FCFS')
        self.assertEqual(self.simulator.executeFCFS(), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511, 5, 15, 40, 65, 20, 35, 400, 90, 100]], 1311, True), 'FCFS')
        self.assertEqual(self.simulator.executeFCFS(), base_results)

    def test_SSTF_shoud_return(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400]], 400, True), 'SSTF')
        self.assertEqual(self.simulator.executeSSTF(), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511, 400, 100, 90, 65, 40, 35, 20, 15, 5]], 506, False), 'SSTF')
        self.assertEqual(self.simulator.executeSSTF(), base_results)

    def test_SCAN_shoud_return(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400]], 400, True), 'SCAN')
        self.assertEqual(self.simulator.executeSCAN(), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511, 400, 100, 90, 65, 40, 35, 20, 15, 5]], 506, False), 'SCAN')
        self.assertEqual(self.simulator.executeSCAN(), base_results)

    def test_CSCAN_shoud_return(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400], []], 400, True), 'CSCAN')
        self.assertEqual(self.simulator.executeCSCAN(), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400]], 400, True), 'CSCAN')
        self.assertEqual(self.simulator.executeCSCAN(), base_results)

    def test_LOOK_shoud_return(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400]], 400, True), 'LOOK')
        self.assertEqual(self.simulator.executeLOOK(), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [511, 400, 100, 90, 65, 40, 35, 20, 15, 5]], 506, False), 'LOOK')
        self.assertEqual(self.simulator.executeLOOK(), base_results)

    def test_CLOOK_shoud_return(self):
        base_results = (([[], [0, 5, 15, 20, 35, 40, 65, 90, 100, 400], []], 400, True), 'CLOOK')
        self.assertEqual(self.simulator.executeCLOOK(), base_results)
        
        self.simulator.init_pos = self.simulator.max_tracks
        base_results = (([[], [self.simulator.max_tracks], [5, 15, 20, 35, 40, 65, 90, 100, 400]], 395, True), 'CLOOK')
        self.assertEqual(self.simulator.executeCLOOK(), base_results)


class TestSimulatorFalseDirection(unittest.TestCase):

    def setUp(self):
        self.simulator = Simulator()
        self.simulator.init_pos = 0
        self.simulator.direction = False
        self.simulator.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]

    def test_dir_post_CSCAN_should_return(self):
        self.simulator.executeCSCAN()
        self.assertEqual(self.simulator.algorithm.last_dir, self.simulator.direction)

    def test_dir_post_CLOOK_should_return(self):
        self.simulator.executeCLOOK()
        self.assertEqual(self.simulator.algorithm.last_dir, self.simulator.direction)

        