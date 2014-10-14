from scheduling import Scheduling


class CSCAN(Scheduling):


    def attend_requirements(self, requirements, init_pos, direction, max_tracks):
        current_pos    = self.startup(requirements, init_pos)
        greater, lower = self.divide_list(self.requirements, current_pos, False)
        self.attended  = []
        if self.page_faults:
            if direction and lower:
                greater.append(max_tracks)
                lower.append(0)
            else:
                if greater:
                    greater.append(max_tracks)
                    lower.append(0)
        else:
            if direction:
                greater.append(init_pos)
                if lower:
                    lower.append(0)
            else:
                lower.append(init_pos)
                if greater:
                    greater.append(max_tracks)
        if direction:
            greater.sort()
            lower.sort()
            self.attended  += greater
            self.movements += self.count_movements(greater, current_pos)
            if lower:
                self.attended  += lower
                self.movements += lower[-1]
            self.last_dir = self.get_end_dir(self.attended, current_pos, init_pos)
            self.greater  = greater
            self.lower    = lower
            return [self.page_faults, self.greater, self.lower], self.movements, direction
        else:
            greater.sort(reverse=True)
            lower.sort(reverse=True)
            self.attended  += lower
            self.movements += current_pos
            if greater:
                self.attended  += greater
                self.movements += max_tracks - greater[-1]
            self.last_dir = self.get_end_dir(self.attended, current_pos, init_pos)
            self.greater  = greater
            self.lower    = lower
            return [self.page_faults, self.lower, self.greater], self.movements, direction