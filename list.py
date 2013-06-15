from random import randint

def random_list(quantity):
    list=[]
    for x in range(0,quantity):
         list.append(randint(0,511))
    return list

def add_random_pf(list, quantity):
    elements = len(list)-1
    for x in range(1,quantity):
        elem = randint(0,elements)
        list[elem] = -list[elem]
    return list

def count_pf(list):
    count = 0
    for elem in list:
        if elem < 0:
            count += 1
    return count


# programa ppal pa test
l = random_list(600)
print l
l = add_random_pf(l,50)
print l
print count_pf(l)