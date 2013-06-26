class Scheduling():

    def attend_requisites():
        pass

    def get_pf(req_list):
        "returns list of page faults and default list without them"
        pf_list = []
        for i in range(len(self.requirements) - 1, -1, -1):  # recorremos en forma inversa para no perer indices
            if self.requirements[i] < 0:
                pf_list.append(abs(self.requirements.pop(i)))
        pf_list.reverse()
        return pf_list

    def startup(req_list):
        self.get_pf()
        if self.page_faults:
            self.movements = momentum(self.page_faults, self.init_pos)
            return self.page_faults[-1]
        else:
            return init_pos
    def momentum(req_list, init_pos):
        """
        calculates movements between each requirement in a list
        
        Keyword arguments:
        req_list (list) -- requirements list

        """
        if req_list:
            movements = abs(req_list[0] - init_pos)
            for index in range(1, len(req_list)):
                movements += abs(req_list[index - 1] - req_list[index])
            return movements
        else:
            return 0

    def divide_list(list, pos, sort=False):
        """
            divides list into < (pos) >
        """
        lower, greater = [], []
        for req in list:
            if req > pos:
                greater.append(req)
            else:
                lower.append(req)
        if sort:
            greater.sort()
            lower.sort(reverse=True)
        return greater, lower

    def get_direction_after_fifo(req_list):

        if (req_list[-1] - req_list[- 2] > 0):
            direction = True
        else:
            direction = False
        return direction