class SSTF(Scheduling):
    """docstring for sstf"""

    def min_distance(list, current_pos):
        list_distances = map(lambda p: abs(p - current_pos), list)
        value = min(list_distances)
        print list_distances
        return list_distances.index(value)

    def attend_requisites(simulator):
        list_req_copy = simulator.requisites[:]
        pf_result = attend_pf(list_req_copy, init_pos, direction)
        served_list = pf_result[0]
        try:
            current_pos = pf_result[0][-1]
        except IndexError:
            current_pos = init_pos
        while list_req_copy:
            index = min_distance(list_req_copy, current_pos)
            current_pos = list_req_copy[index]
            served_list.append(list_req_copy.pop(index))
        movements = momentum(pf_result[0], init_pos)
        return (served_list, movements)

