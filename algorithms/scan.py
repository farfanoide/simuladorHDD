class SCAN():


    def attend_requisites():
        pf_result = attend_pf(list, init_pos, direction)
        try:
            last_pf = pf_result[0][-1]
        except:
            last_pf = init_pos
        direction = pf_result[2]
        (greater, lower) = divide_list(list, last_pf, True)
        served_list = pf_result[0]
        if direction:
            served_list.extend(greater)
            served_list.extend(lower)
            try:
                movements = (511 - greater[-1]) * 2
            except IndexError:
                movements = (511 - last_pf) * 2

        else:
            served_list.extend(lower)
            served_list.extend(greater)
            try:
                movements = lower[-1] * 2
            except IndexError:
                movements = last_pf * 2
        movements += momentum(served_list, init_pos)
        return(served_list, movements, not direction)