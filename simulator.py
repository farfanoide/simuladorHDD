from random import randint
import math
class Simulator():
    """Simulates Scheduling Algorithms"""
    

    def __init__(self, reqs=[], pos=250, dire=True, tracks=511):
        self.requirements = reqs
        self.init_pos = pos
        self.direction = dire
        self.max_tracks = tracks
        self.movements = 0
        self.page_faults = []
        self.served_reqs = []

    
    def executeFCFS():
        algorithm = Fcfs()
        algorithm.attend_requisites(self)
    
    def executeSSTF():
        algorithm = Sstf()
        algorithm.attend_requisites(self)
    
    def executeSCAN():
        algorithm = Scan()
        algorithm.attend_requisites(self)
    
    def executeCSCAN():
        algorithm = CScan()
        algorithm.attend_requisites(self)
    
    def executeLOOK():
        algorithm = Look()
        algorithm.attend_requisites(self)
    
    def executeCLOOK():
        algorithm = CLook()
        algorithm.attend_requisites(self)

    #-------------
    # Common
    #-------------
    def fifo(req_list, init_pos, direction):

        if req_list:
            if (req_list[-1] - req_list[- 2] > 0):
                direction = True
            else:
                direction = False
            movements = momentum(req_list, init_pos)
            return(req_list, movements, direction)
        else:
            return(req_list, 0, direction)



    


    # def attend_pf(list, init_pos, direction):
    #     pf_list = get_pf(list)
    #     return fifo(pf_list, init_pos, direction)


    def add_random_pf(self, quantity):
        for x in range(quantity):
            elem = randint(0,len(self.requirements)-1)
            self.requirements[elem] = -self.requirements[elem]




    #-------------
    # end Common
    #-------------