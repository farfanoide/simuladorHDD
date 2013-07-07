from scheduling import Scheduling
class SCAN(Scheduling):


    def attend_requirements(self, requirements, init_pos, direction, max_tracks):

        current_pos    = self.startup(requirements, init_pos)
        greater, lower = self.divide_list(self.requirements, current_pos, True)
        post_pf_dir    = self.get_end_dir(self.page_faults, init_pos, direction)
        if post_pf_dir:
            greater.append(max_tracks)
            self.attended += greater
            self.attended += lower
        else:
            lower.append(0)
            self.attended += lower
            self.attended += greater
        self.movements += self.count_movements(self.attended, self.get_last_req(self.page_faults, init_pos))
        return [self.page_faults, self.attended], self.movements, not post_pf_dir