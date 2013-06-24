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


    def get_pf(self):
        "returns list of page faults and default list without them"
        pf_list = []
        for i in range(len(self.requirements) - 1, -1, -1):  # recorremos en forma inversa para no perer indices
            if self.requirements[i] < 0:
                pf_list.append(abs(self.requirements.pop(i)))
        pf_list.reverse()
        self.page_faults = pf_list

    def startup(self):
        self.get_pf()
        if self.page_faults:
            self.movements = momentum(self.page_faults, self.init_pos)
            return self.page_faults[-1]
        else:
            return init_pos
    


    # def attend_pf(list, init_pos, direction):
    #     pf_list = get_pf(list)
    #     return fifo(pf_list, init_pos, direction)


        

    def random_list(self, quantity):
        """Generates random list, duh!

        Keyword arguments:
        quantity (int) -- amount of numbers 

        """
        return [randint(0,self.max_tracks) for i in range(quantity)]


    def add_random_pf(self, quantity):
        for x in range(quantity):
            elem = randint(0,len(self.requirements)-1)
            self.requirements[elem] = -self.requirements[elem]





    def divide_list(list, pos, sort=False):
        """
            divides list into < (pos) >
        """
        lower, greater = [], []
        for req in list:
            if req > pos:
                greater.append(req)
            else:
                lower.append(req)
        if sort:
            greater.sort()
            lower.sort(reverse=True)
        return greater, lower

    def min_distance(list, current_pos):
        list_distances = map(lambda p: abs(p - current_pos), list)
        value = min(list_distances)
        print list_distances
        return list_distances.index(value)


    #-------------
    # end Common
    #-------------