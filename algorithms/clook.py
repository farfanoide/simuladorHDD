from scheduling import Scheduling


class CLOOK(Scheduling):


    def attend_requirements(self, requirements, init_pos, direction):
        current_pos    = self.startup(requirements, init_pos)
        greater, lower = self.divide_list(self.requirements, current_pos)
        if not self.page_faults:
            if direction:
                greater.append(init_pos)
            else:
                lower.append(init_pos)
        if direction:
            if greater:
                greater.sort()
                self.attended  += greater
                self.movements += self.count_movements(greater, current_pos)
            if lower:
                lower.sort()
                self.attended  += lower
                self.movements += self.count_movements(lower, lower[0])
            self.last_dir = self.get_end_dir(self.attended, current_pos, direction)
            self.greater  = greater
            self.lower    = lower
            return [self.page_faults, self.greater, self.lower], self.movements, self.last_dir
        else:
            if lower:
                lower.sort(reverse=True)
                self.attended.extend(lower)
                self.movements += self.count_movements(lower, current_pos)
            if greater:
                greater.sort(reverse=True)
                self.attended.extend(greater)
                self.movements += self.count_movements(greater, greater[0])
            self.last_dir = self.get_end_dir(self.attended, current_pos, direction)
            self.greater  = greater
            self.lower    = lower
            return [self.page_faults, self.lower, self.greater], self.movements, self.last_dir
