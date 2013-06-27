from scheduling import Scheduling
class LOOK(Scheduling):

    
    def attend_requirements(self, requirements, init_pos, direction):

        current_pos    = self.startup(requirements, init_pos)
        greater, lower = self.divide_list(requirements, current_pos, sort=True)
        post_pf_dir    = self.get_end_dir(self.page_faults, init_pos, direction)
        if post_pf_dir:
            self.attended += greater
            self.attended += lower
        else:
            self.attended += lower
            self.attended += greater
        self.movements += self.count_movements(self.attended, init_pos)
        return(self.attended, self.movements, not post_pf_dir)