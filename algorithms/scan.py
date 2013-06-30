from scheduling import Scheduling
class SCAN(Scheduling):


    def attend_requirements(self, requirements, init_pos, direction, max_tracks):

        current_pos    = self.startup(requirements, init_pos)
        greater, lower = self.divide_list(self.requirements, current_pos, True)
        post_pf_dir    = self.get_end_dir(self.page_faults, init_pos, direction)
        results = []
        results.append(self.page_faults)
        if post_pf_dir:
            greater.append(max_tracks)
            self.attended += greater
            self.attended += lower
            results.append(self.attended)
            try:
                self.movements += (max_tracks - greater[-2]) * 2
            except IndexError:
                self.movements += (max_tracks - current_pos) * 2
        else:
            lower.append(0)
            self.attended += lower
            self.attended += greater
            results.append(self.attended)
            try:
                self.movements += lower[-2] * 2
            except IndexError:
                self.movements += current_pos * 2
        self.movements += self.count_movements(self.attended, init_pos)
        return results, self.movements, not post_pf_dir