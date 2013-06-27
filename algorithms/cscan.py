class CSCAN(Scheduling):

    
    def attend_requirements(self, requirements, init_pos, direction):
        pf_result = attend_pf(list, init_pos, direction)
        try:
            last_pf = pf_result[0][-1]
        except:
            last_pf = init_pos
        sorted_lists = divide_list(list, last_pf, False)
        greater = sorted_lists[0]
        lower = sorted_lists[1]
        served_list = pf_result[0]
        movements = momentum(pf_result[0], init_pos)
        if direction:
            greater.sort()
            lower.sort()
            served_list.extend(greater)
            served_list.append(511)

            movements += 511 - last_pf
            if len(lower) > 0:
                served_list.extend(lower)
                movements += lower[-1]
        else:
            greater.sort(reverse=True)
            lower.sort(reverse=True)
            served_list.extend(lower)
            served_list.append(0)
            movements += last_pf  # agregamos el ultimo elem para compensar la distancia
            if len(greater) > 0:
                served_list.extend(greater)
                movements += 511 - greater[-1]
        return (served_list, movements, direction)