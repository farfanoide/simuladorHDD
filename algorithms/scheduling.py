class Scheduling():

    def __init__(self):
        self.requirements = []
        self.attended = []
        self.page_faults = []
        self.movements = 0
        self.direction = True
        self.last_dir = True

    def get_attended_requirements(self):
        return self.requirements

    def get_movements(self):
        return self.movements

    def get_direction(self):
        return self.direction

    def attend_requirements(self, requirements, init_pos, direction):
        pass

    def get_pfs(self, requirements):
        "returns list of page faults"

        for req in requirements:
            if req < 0:
                self.page_faults.append(abs(req))
            else:
                self.requirements.append(req)

    def startup(self, requirements, init_pos):
        """
        Initializes
        """
        self.get_pfs(requirements)
        if self.page_faults:
            self.movements += self.count_movements(self.page_faults, init_pos)
            # self.attended += self.page_faults
            return self.page_faults[-1]
        else:
            # there arent any page faults
            try:
                self.movements = abs(self.requirements[0] - init_pos)
            except IndexError:
            # there arent any requirements
                pass
            return init_pos

    def count_movements(self, requirements, init_pos):
        """
        calculates movements between each requirement in a list

        Keyword arguments:
        requirements (list) -- requirements list

        """
        if requirements:
            movements = abs(requirements[0] - init_pos)
            for index in range(1, len(requirements)):
                movements += abs(requirements[index - 1] - requirements[index])
            return movements
        else:
            return 0

    def divide_list(self, requirements, pos, sort=False):
        """
            divides list into < (pos) >
        """
        lower, greater = [], []
        for req in requirements:
            if req > pos:
                greater.append(req)
            else:
                lower.append(req)
        if sort:
            greater.sort()
            lower.sort(reverse=True)
        return greater, lower

    def get_end_dir(self, requirements, init_pos, orig_dir):

        try:
            if len(requirements) > 1:
                if (requirements[-1] - requirements[- 2] > 0):
                    direction = True
                else:
                    direction = False
            else:
                if (requirements[0] - init_pos > 0):
                    direction = True
                else:
                    direction = False
            return direction
        except IndexError:
            return orig_dir

    def get_last_req(self, requirements, init_pos):
        if requirements:
            return requirements[-1]
        else:
            return init_pos
