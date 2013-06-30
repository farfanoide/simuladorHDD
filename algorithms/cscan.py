from scheduling import Scheduling
class CSCAN(Scheduling):

    
    def attend_requirements(self, requirements, init_pos, direction, max_tracks):
        current_pos    = self.startup(requirements, init_pos)
        greater, lower = self.divide_list(self.requirements, current_pos, False)
        post_pf_dir    = self.get_end_dir(self.page_faults, init_pos, direction)
        lower += [0]
        greater += [max_tracks]
        if post_pf_dir:
            greater.sort()
            lower.sort()
            # add last track
            # self.attended  += [max_tracks]
            self.attended  += greater
            self.movements += max_tracks - current_pos
            if lower:
                self.attended  += lower
                self.movements += lower[-1]
            return [self.page_faults, greater, lower], self.movements, post_pf_dir
        else:
            # lower += [0]
            # greater += [max_tracks]
            greater.sort(reverse=True)
            lower.sort(reverse=True)
            # self.attended  += [0]
            # add firs track 
            self.attended  += lower
            self.movements += current_pos  
            if greater:
                self.attended  += greater
                self.movements += max_tracks - greater[-1]
            return [self.page_faults, lower, greater], self.movements, post_pf_dir