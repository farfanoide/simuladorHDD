from random import randint
import algorithms
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty


class Simulator(EventDispatcher):

    """Simulates Scheduling algorithms"""

    algorithm = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.requirements = kwargs.get('reqs', [])
        self.init_pos = kwargs.get('pos', 250)
        self.direction = kwargs.get('dire', True)
        self.max_tracks = kwargs.get('tracks', 511)

    def set_requirements(self, requirements):
        if requirements and type(requirements) == list:
            self.requirements = []
            for req in requirements:
                if abs(req) <= self.max_tracks:
                    self.requirements.append(req)



    def execute_algorithm(self, algorithm):
        class_ = getattr(algorithms, algorithm)
        temp = class_()
        if "SCAN" in algorithm:
            return temp.attend_requirements(
                self.requirements, self.init_pos, self.direction, self.max_tracks), algorithm
        else:
            return temp.attend_requirements(
                self.requirements, self.init_pos, self.direction), algorithm

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

    def remove_pf(self):
        """Removes all Page Faults in current requierement list"""

        for i in range(len(self.requirements)):
            if (self.requirements[i] < 0):
                self.requirements[i] = -self.requirements[i]
