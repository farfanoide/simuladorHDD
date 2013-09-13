from random import randint
import math
from algorithms import *
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty

class Simulator(EventDispatcher):

    """Simulates Scheduling algorithms"""

    algorithm = ObjectProperty(None)

    def __init__(self, reqs=[], pos=250, dire=True, tracks=511):
        self.requirements = reqs
        self.init_pos = pos
        self.direction = dire
        self.max_tracks = tracks

    # TODO: simplify all executeXXXX
    def executeFCFS(self):
        algorithm = FCFS()
        return algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction), "FCFS"

    def executeSSTF(self):
        self.algorithm = SSTF()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction), "SSTF"

    def executeSCAN(self):
        self.algorithm = SCAN()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction, self.max_tracks), "SCAN"

    def executeCSCAN(self):
        self.algorithm = CSCAN()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction, self.max_tracks), "CSCAN"

    def executeLOOK(self):
        self.algorithm = LOOK()
        return self.algorithm.attend_requirements(
            self.requirements, self.init_pos, self.direction), "LOOK"

    def executeCLOOK(self):
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

    # TODO: implement remove_pf
    # def remove_pf(self):
    #     for req in self.requirements:
    #         if (req < 0):
    #             print req
    #             req = -req
