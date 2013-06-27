from scheduling import Scheduling
class SSTF(Scheduling):
    """docstring for sstf"""

    def get_min_distance(self, requirements, current_pos):
        distances = map(lambda p: abs(p - current_pos), requirements)
        min_distance = min(distances)
        return distances.index(min_distance)

    def attend_requirements(self, requirements, init_pos, direction):
        current_pos   = self.startup(requirements, init_pos)
        self.attended = self.page_faults[:]
        reqs_copy     = self.requirements[:]
        while reqs_copy:
            index       = self.get_min_distance(reqs_copy, current_pos)
            current_pos = reqs_copy[index]
            self.attended.append(reqs_copy.pop(index))
        self.movements = self.count_movements(self.attended, init_pos) 
        self.last_dir  = self.get_end_dir(self.attended, init_pos, direction)
        return (self.attended, self.movements, self.last_dir)