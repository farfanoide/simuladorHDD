class look():
    def LOOK(list, init_pos, direction):
        pf_result = attend_pf(list, init_pos, direction)
        try:
            current_pos = pf_result[0][-1]
        except:
            current_pos = init_pos
        direction = pf_result[2]
        served_list = pf_result[0]
        (greater, lower) = divide_list(list, current_pos, True)

        if direction:
            served_list.extend(greater)
            served_list.extend(lower)
        else:
            served_list.extend(lower)
            served_list.extend(greater)
        movements = momentum(served_list, init_pos)
        return(served_list, movements, not direction)