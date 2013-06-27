from scheduling import Scheduling
class SCAN(Scheduling):


    def attend_requirements(self, requirements, init_pos, direction, max_tracks):

        current_pos    = self.startup(requirements, init_pos)
        greater, lower = self.divide_list(self.requirements, current_pos, True)
        try:
            post_pf_dir  = self.get_end_dir(self.page_faults)
        except IndexError:
            post_pf_dir = direction
        if post_pf_dir:
            self.attended += greater
            self.attended += lower
            try:
                self.movements += (max_tracks - greater[-1]) * 2
            except IndexError:
                self.movements += (max_tracks - current_pos) * 2

        else:
            self.attended += lower
            self.attended += greater
            try:
                self.movements += lower[-1] * 2
            except IndexError:
                self.movements += current_pos * 2
        self.movements += self.count_movements(self.attended, init_pos)
        return(self.attended, self.movements, not post_pf_dir)