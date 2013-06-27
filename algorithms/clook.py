from scheduling import Scheduling
class CLOOK(Scheduling):

    
    def attend_requirements(self, requirements, init_pos, direction):
        current_pos      = self.startup(requirements, init_pos)
        self.movements   = self.count_movements(self.page_faults, init_pos)
        (greater, lower) = self.divide_list(requirements, current_pos)
        direction        = self.get_end_dir(self.page_faults)
        if direction:
            greater.sort()
            lower.sort()
            self.attended  += greater
            self.attended  += lower
            self.movements += self.count_movements(greater, current_pos)
            self.movements += self.count_movements(lower, lower[0])

        else:
            greater.sort(reverse=True)
            lower.sort(reverse=True)
            self.attended.extend(lower)
            self.attended.extend(greater)
            self.movements += self.count_movements(lower, current_pos)
            self.movements += self.count_movements(greater, greater[0])
        return (self.attended, self.movements, direction)