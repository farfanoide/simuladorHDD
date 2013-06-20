from random import randint
import math


def random_list(quantity):
    list = []
    for x in range(0, quantity):
        list.append(randint(0, 511))
    return list


def add_random_pf(list, quantity):
    for x in range(0, quantity):
        elem = randint(0, len(l) - 1)
        list[elem] = list[elem] * -1
    return list


def momentum(list, init_pos):
    if len(list) > 0:
        mov = abs(list[0] - init_pos)
        for index in range(1, len(list)):
            mov = mov + abs(list[index - 1] - list[index])
        return mov
    else:
        return 0


def fifo(list, init_pos, direction):
    "receives a list, initial position and direction. returns list ordered as served by algorithm, amount of movements and direction"
    # Final direction set
    if len(list) > 0:
        leindex = len(list) - 1  # last element index
        if (list[leindex] - list[leindex - 1] > 0):
            direction = True
        else:
            direction = False
        sum = momentum(list, init_pos)
        return(list, sum, direction)
    else:
        return(list, 0, direction)


def get_pf(list):
    "returns list of page faults and default list without them"
    list_pf = []
    for i in range(len(list) - 1, -1, -1):  # recorremos en forma inversa para no perer indices
        if list[i] < 0:
            list_pf.append(abs(list.pop(i)))
    list_pf.reverse()
    return list_pf


def attend_pf(list, init_pos, direction):
    pf_list = get_pf(list)
    return fifo(pf_list, init_pos, direction)

# FCFS  implementation


def FCFS(list, init_pos, direction):
    pf_result = attend_pf(list, init_pos, direction)
    fifo_result = fifo(list, pf_result[0][-1], pf_result[2])
    pf_result[0].extend(fifo_result[0])

    return (pf_result[0], momentum(pf_result[0], init_pos), fifo_result[2])


def min_dist(list, current_pos):
    list_distances = map(lambda p: abs(p - current_pos), list)
    value = min(list_distances)
    print list_distances
    return list_distances.index(value)


def SSTF(list_req, init_pos, direction):
    list_req_copy = list_req[:]
    list_req_attended = []
    pf_result = attend_pf(list_req_copy, init_pos, direction)
    current_pos = pf_result[0][-1]
    while (len(list_req_copy) > 0):
        index = min_dist(list_req_copy, current_pos)
        current_pos = list_req_copy[index]
        list_req_attended.append(list_req_copy.pop(index))
    pf_result[0].extend(list_req_attended)
    return (pf_result[0], momentum(pf_result[0], init_pos))

#   SCAN (lista, posicion inicial, direccion.)
    # copiamos lista
    # obtener_proximo -> devuelve indice del proximo


def divide_list(list, pos, sort=False):
    """
        divides list into < (pos) >
    """
    lower = []
    greater = []
    for req in list:
        if req > pos:
            greater.append(req)
        else:
            lower.append(req)
    if sort:
        greater.sort()
        lower.sort(reverse=True)
    return (greater, lower)


def SCAN(list, init_pos, direction):
    pf_result = attend_pf(list, init_pos, direction)
    direction = pf_result[2]
    last_pf = pf_result[0][-1]
    sorted_lists = divide_list(list, last_pf, True)
    served_list = pf_result[0]
    greater = sorted_lists[0]
    lower = sorted_lists[1]
    # TODO: destroy pf_result
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
    # direction = !direction
    movements += momentum(served_list, init_pos)
    return(served_list, movements, not direction)


def CSCAN(list, init_pos, direction):
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
        movements += 511 - last_pf
        if len(lower) > 0:
            served_list.extend(lower)
            movements += lower[-1]
    else:
        greater.sort(reverse=True)
        lower.sort(reverse=True)
        served_list.extend(lower)
        movements += last_pf  # agregamos el ultimo elem para compensar la distancia
        if len(greater) > 0:
            served_list.extend(greater)
            movements += 511 - greater[-1]
    return (served_list, movements, direction)


# TODO: preguntar destroy
# TODO: preguntar web 0 pygame 0 xxx
# TODO: preguntar cuando se entrega
# Data conversor
# TESTS
# print "testeando fifo"
# lachota = [200,150,400,35]
# tupla = fifo(lachota, 100, True)
# print tupla
# print "fin test fifo"
# print "test get_pf"
# l=random_list(10)
# add_random_pf(l,3)
# pfss=get_pf(l)
# print pfss
# print "test FCFS"
# lsstf = [399, 190, 120, -450, 350, 511, -12]
# print SSTF(lsstf, 1, False)
# print "fin"
# print "test momentum and min"
# l=[15,10,30,40,14]
# i=0
# print momentum(l,i)
# print l
# print min_dist(l,9)
# print "end test FCFS"
lsstf = [280, 406, 161, 444, 0]
# lsstf = random_list(5)
print lsstf
# print "test divides"
# print divide_list(lsstf, 150)
print "test CSCAN"
print CSCAN(lsstf, 250, False)
print "fin SCAN"

