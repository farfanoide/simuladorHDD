from scheduling import Scheduling


class FCFS(Scheduling):

        def attend_requirements(self, requirements, init_pos, direction):

                current_pos = self.startup(requirements, init_pos)
                self.attended += self.requirements
                self.movements += self.count_movements(self.requirements, current_pos)
                self.last_dir = self.get_end_dir(self.requirements, init_pos, direction)
                return [self.page_faults, self.attended], self.movements, self.last_dir
