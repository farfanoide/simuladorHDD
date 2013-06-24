class clook():
    def attend_requisites(simulator):
        pf_result = attend_pf(list, init_pos, direction)
        try:
            current_pos = pf_result[0][-1]
        except:
            current_pos = init_pos
        served_list = pf_result[0]
        movements = momentum(served_list, init_pos)
        (greater, lower) = divide_list(list, current_pos)
        if direction:
            greater.sort()
            lower.sort()
            served_list.extend(greater)
            served_list.extend(lower)
            movements += momentum(greater, current_pos)
            movements += momentum(lower, lower[0])

        else:
            greater.sort(reverse=True)
            lower.sort(reverse=True)
            served_list.extend(lower)
            served_list.extend(greater)
            movements += momentum(lower, current_pos)
            movements += momentum(greater, greater[0])
        return (served_list, movements, direction)