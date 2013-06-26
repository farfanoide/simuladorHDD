class FCFS(Scheduling):


        def attend_requisites(simulator):
                current_pos = self.startup(simulator)
                self.served_reqs += self.page_faults + self.requirements
                self.movements += momentum(self.requirements, current_pos)
                
                # try:
                #     current_pos = pf_result[0][-1]
                #     served_list = pf_result[0]
                # except IndexError:
                #     current_pos = init_pos
                #     served_list = []
                # fifo_result = fifo(list, current_pos, pf_result[2])
                # served_list.extend(fifo_result[0])
                # return (served_list, movements, fifo_result[2])
