from scheduling import Scheduling
class SSTF(Scheduling):
    """docstring for sstf"""

    def get_min_distance(requirements, current_pos):
        distances = map(lambda p: abs(p - current_pos), requirements)
        min_distance = min(distances)
        return distances.index(min_distance)

    def attend_requirements(requirements, init_pos, direction):
        reqs_copy = self.att_reqs[:]
        current_pos = self.startup(requirements, init_pos)
        # pf_result = attend_pf(reqs_copy, init_pos, direction)
        # served_list = pf_result[0]
        # try:
        #     current_pos = pf_result[0][-1]
        # except IndexError:
        #     current_pos = init_pos
        while reqs_copy:
            index = get_min_distance(reqs_copy, current_pos)
            current_pos = reqs_copy[index]
            served_list.append(reqs_copy.pop(index))
        movements = momentum(pf_result[0], init_pos)
        return (served_list, movements)

