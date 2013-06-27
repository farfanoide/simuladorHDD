from random import randint
import math


class Simulator():

    """Simulates Scheduling Algorithms"""

    def __init__(self, reqs=[], pos=250, dire=True, tracks=511):
        self.requirements = reqs
        self.init_pos = pos
        self.direction = dire
        self.max_tracks = tracks

    def executeFCFS(self):
        from algorithms.fcfs import FCFS
        algorithm = FCFS()
        return algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction)

    def executeSSTF(self):
        algorithm = Sstf()
        algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction)

    def executeSCAN(self):
        algorithm = Scan()
        algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction)

    def executeCSCAN(self):
        algorithm = CScan()
        algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction)

    def executeLOOK(self):
        algorithm = Look()
        algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction)

    def executeCLOOK(self):
        algorithm = CLook()
        algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction)

    #-------------
    # Common
    #-------------

    # def attend_pf(list, init_pos, direction):
    #     pf_list = get_pf(list)
    #     return fifo(pf_list, init_pos, direction)
    def random_list(self, quantity):
        """Generates random list, duh!

        Keyword arguments:
        quantity (int) -- length of the requirement list

        """
        self.requirements = [randint(
            0, self.max_tracks) for i in range(quantity)]

    def add_random_pf(self, quantity):
        for x in range(quantity):
            elem = randint(0, len(self.requirements) - 1)
            self.requirements[elem] = -self.requirements[elem]




    #-------------
    # end Common
    #-------------
