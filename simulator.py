from random import randint
import math


class Simulator():

    """Simulates Scheduling algorithms"""

    def __init__(self, reqs=[], pos=250, dire=True, tracks=511):
        self.requirements = reqs
        self.init_pos = pos
        self.direction = dire
        self.max_tracks = tracks

    def executeFCFS(self):
        from algorithms.fcfs import FCFS
        self.algorithm = FCFS()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction), "FCFS"

    def executeSSTF(self):
        from algorithms.sstf import SSTF
        self.algorithm = SSTF()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction), "SSTF"

    def executeSCAN(self):
        from algorithms.scan import SCAN
        self.algorithm = SCAN()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction, self.max_tracks), "SCAN"

    def executeCSCAN(self):
        from algorithms.cscan import CSCAN
        self.algorithm = CSCAN()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction, self.max_tracks), "CSCAN"

    def executeLOOK(self):
        from algorithms.look import LOOK
        self.algorithm = LOOK()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction), "LOOK"

    def executeCLOOK(self):
        from algorithms.clook import CLOOK
        self.algorithm = CLOOK()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction), "CLOOK"

    def random_list(self, quantity):
        """
        Generates random list, duh!

        Keyword arguments:
        quantity (int) -- Length of the requirement list

        """
        self.requirements = [randint(
            0, self.max_tracks) for i in range(quantity)]

    def add_random_pf(self, quantity):
        """
        Adds page faults at random positions

        Keyword arguments:
        quantity (int) -- Amount of page faults to create

        """
        for x in range(quantity):
            elem = randint(0, len(self.requirements) - 1)
            self.requirements[elem] = -self.requirements[elem]
