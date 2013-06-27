from scheduling import Scheduling
class CSCAN(Scheduling):

    
    def attend_requirements(self, requirements, init_pos, direction, max_tracks):
        current_pos    = self.startup(requirements, init_pos)
        greater, lower = self.divide_list(attend_requirements, current_pos, False)
        direction      = self.get_end_dir(self.page_faults)
        if direction:
            greater.sort()
            lower.sort()
            self.attended  += greater
            # add last track
            self.attended  += [max_tracks]
            self.movements += max_tracks - current_pos
            if lower:
                self.attended  += lower
                self.movements += lower[-1]
        else:
            greater.sort(reverse=True)
            lower.sort(reverse=True)
            self.attended  += lower
            # add firs track 
            self.attended  += [0]
            self.movements += current_pos  
            if greater:
                self.attended  += greater
                self.movements += max_tracks - greater[-1]
        return (self.attended, self.movements, direction)