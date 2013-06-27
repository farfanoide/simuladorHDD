from scheduling import Scheduling
class CLOOK(Scheduling):

    
    def attend_requirements(self, requirements, init_pos, direction):
        current_pos    = self.startup(requirements, init_pos)
        self.movements = self.count_movements(self.page_faults, init_pos)
        greater, lower = self.divide_list(self.requirements, current_pos)
        post_pf_dir    = self.get_end_dir(self.page_faults, init_pos, direction)

        if post_pf_dir:
            if greater:
                greater.sort()
                self.attended  += greater
                self.movements += self.count_movements(greater, current_pos)
            if lower:
                lower.sort()
                self.attended  += lower
                self.movements += self.count_movements(lower, lower[0])
        else:
            if lower:
                lower.sort(reverse=True)
                self.attended.extend(lower)
                self.movements += self.count_movements(lower, current_pos)
            if greater:
                greater.sort(reverse=True)
                self.attended.extend(greater)
                self.movements += self.count_movements(greater, greater[0])
        return (self.attended, self.movements, post_pf_dir)