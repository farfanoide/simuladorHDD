from random import randint
import math
class Simulator():
    """docstring for simulator"""
    

    def __init__(self, reqs = [], tracks = 511):
        self.requirements = reqs
        self.max_tracks = tracks
                       
    def random_list(quantity, max):
        """Generates random list, duh!

        Keyword arguments:
        quantity (int) -- amount of numbers 

        """
        reqs = []
        for x in range(0, quantity):
            reqs.append(randint(0, self.max_tracks))
        return reqs


    def add_random_pf(list, quantity):
        for x in range(0, quantity):
            elem = randint(0, len(l) - 1)
            list[elem] = list[elem] * -1
        return list


    def momentum(req_list, init_pos):
        """
        calculates movements between each requirement in a list
        :param list: list
        """
        if req_list:
            mov = abs(req_list[0] - init_pos)
            for index in range(1, len(req_list)):
                mov = mov + abs(req_list[index - 1] - req_list[index])
            return mov
        else:
            return 0


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


    def get_pf(list):
        "returns list of page faults and default list without them"
        list_pf = []
        for i in range(len(list) - 1, -1, -1):  # recorremos en forma inversa para no perer indices
            if list[i] < 0:
                list_pf.append(abs(list.pop(i)))
        list_pf.reverse()
        return list_pf


    def attend_pf(list, init_pos, direction):
        pf_list = get_pf(list)
        return fifo(pf_list, init_pos, direction)


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


    def FCFS(list, init_pos, direction):
        pf_result = attend_pf(list, init_pos, direction)
        try:
            current_pos = pf_result[0][-1]
            served_list = pf_result[0]
        except IndexError:
            current_pos = init_pos
            served_list = []
        fifo_result = fifo(list, current_pos, pf_result[2])
        served_list.extend(fifo_result[0])
        movements = momentum(served_list, init_pos)
        return (served_list, movements, fifo_result[2])


    def min_distance(list, current_pos):
        list_distances = map(lambda p: abs(p - current_pos), list)
        value = min(list_distances)
        print list_distances
        return list_distances.index(value)


    def SSTF(list_req, init_pos, direction):
        list_req_copy = list_req[:]
        list_req_attended = []
        pf_result = attend_pf(list_req_copy, init_pos, direction)
        try:
            current_pos = pf_result[0][-1]
        except IndexError:
            current_pos = init_pos

        while (len(list_req_copy) > 0):
            index = min_distance(list_req_copy, current_pos)
            current_pos = list_req_copy[index]
            list_req_attended.append(list_req_copy.pop(index))
        pf_result[0].extend(list_req_attended)
        return (pf_result[0], momentum(pf_result[0], init_pos))


    def SCAN(list, init_pos, direction):
        pf_result = attend_pf(list, init_pos, direction)
        try:
            last_pf = pf_result[0][-1]
        except:
            last_pf = init_pos
        direction = pf_result[2]
        (greater, lower) = divide_list(list, last_pf, True)
        served_list = pf_result[0]
        if direction:
            served_list.extend(greater)
            served_list.extend(lower)
            try:
                movements = (511 - greater[-1]) * 2
            except IndexError:
                movements = (511 - last_pf) * 2

        else:
            served_list.extend(lower)
            served_list.extend(greater)
            try:
                movements = lower[-1] * 2
            except IndexError:
                movements = last_pf * 2
        movements += momentum(served_list, init_pos)
        return(served_list, movements, not direction)


    def CSCAN(list, init_pos, direction):
        pf_result = attend_pf(list, init_pos, direction)
        try:
            last_pf = pf_result[0][-1]
        except:
            last_pf = init_pos
        sorted_lists = divide_list(list, last_pf, False)
        greater = sorted_lists[0]
        lower = sorted_lists[1]
        served_list = pf_result[0]
        movements = momentum(pf_result[0], init_pos)
        if direction:
            greater.sort()
            lower.sort()
            served_list.extend(greater)
            served_list.append(511)

            movements += 511 - last_pf
            if len(lower) > 0:
                served_list.extend(lower)
                movements += lower[-1]
        else:
            greater.sort(reverse=True)
            lower.sort(reverse=True)
            served_list.extend(lower)
            served_list.append(0)
            movements += last_pf  # agregamos el ultimo elem para compensar la distancia
            if len(greater) > 0:
                served_list.extend(greater)
                movements += 511 - greater[-1]
        return (served_list, movements, direction)


    def LOOK(list, init_pos, direction):
        pf_result = attend_pf(list, init_pos, direction)
        try:
            current_pos = pf_result[0][-1]
        except:
            current_pos = init_pos
        direction = pf_result[2]
        served_list = pf_result[0]
        (greater, lower) = divide_list(list, current_pos, True)

        if direction:
            served_list.extend(greater)
            served_list.extend(lower)
        else:
            served_list.extend(lower)
            served_list.extend(greater)
        movements = momentum(served_list, init_pos)
        return(served_list, movements, not direction)


    def CLOOK(list, init_pos, direction):
        pf_result = attend_pf(list, init_pos, direction)
        try:
            current_pos = pf_result[0][-1]
        except:
            current_pos = init_pos
        served_list = pf_result[0]
        movements = momentum(served_list, init_pos)
        (greater, lower) = divide_list(list, current_pos)
        if direction:
            greater.sort()
            lower.sort()
            served_list.extend(greater)
            served_list.extend(lower)
            movements += momentum(greater, current_pos)
            movements += momentum(lower, lower[0])

        else:
            greater.sort(reverse=True)
            lower.sort(reverse=True)
            served_list.extend(lower)
            served_list.extend(greater)
            movements += momentum(lower, current_pos)
            movements += momentum(greater, greater[0])
        return (served_list, movements, direction)

