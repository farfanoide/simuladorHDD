class scheduling():

    def attend_requisites():
        pass

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