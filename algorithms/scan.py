from shceduling import Scheduling
class SCAN(Scheduling):


    def attend_requirements(self, requirements, init_pos, direction):

        current_pos = self.startup(requirements, init_pos)
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