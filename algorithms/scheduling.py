
class Scheduling(object):

    """ Base Class for all algorithms """

    def __init__(self):
        self.requirements = []
        self.attended     = []
        self.page_faults  = []
        self.greater      = []
        self.lower        = []
        self.movements    = 0
        self.direction    = True
        self.last_dir     = None

    def attend_requirements(self, requirements, init_pos, direction):
        pass

    def extract_page_faults(self, requirements):
        """
        Removes page faults from original requirement list
        and saves them to their own to be attended.
        """
        if requirements:
            for req in requirements:
                if req < 0:
                    self.page_faults.append(abs(req))
                else:
                    self.requirements.append(req)
        else:
            return None

    def startup(self, requirements, init_pos):
        """
        Initializes the simulation movementes and page faults

        Keyword arguments:
        requirements (list) -- List of requirements
        init_pos (integer)  -- Initial position
        """
        self.extract_page_faults(requirements)
        if self.page_faults:
            self.page_faults = [init_pos] + self.page_faults
            self.movements += self.count_movements(self.page_faults, init_pos)
            return self.page_faults[-1]
        else:
            self.attended.append(init_pos)
            return init_pos

    def count_movements(self, requirements, init_pos):
        """
        Calculates movements between each requirement in a list.

        Keyword arguments:
        requirements (list) -- List of requirements
        init_pos (integer)  -- Initial position

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
        Splits a list of requirements and returns one greater than
        the initial position and one lower.

        Keyword arguments:
        requirements (list) -- List of requirements
        pos (integer)  -- Splitting position
        sort (boolean) -- Sort lists before return

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
        """
        Checks and returns final direction in al list of requirements.

        Keyword arguments:
        requirements (list) -- List of requirements
        init_pos (integer)  -- Initial position in case the list has too few requirements
        orig_dir (integer)  -- Original directino in case the list has not enough requirements

        """

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
