from random import randint
import math
def random_list(quantity):
    list=[]
    for x in range(0,quantity):
         list.append(randint(0,511))
    return list

def add_random_pf(list, quantity):
    for x in range(0,quantity):
        elem = randint(0,len(l)-1)
        list[elem] = list[elem] *-1
    return list


def fifo(list, init_pos, direction):
    "receives a list, initial position and direction. returns list ordered as served by algorithm, amount of movements and direction"
    # Final direction set
    leindex = len(list)-1                   #last element index
    if (list[leindex]-list[leindex-1]>0):
        direction = True
    else:
        direction = False

    sum = abs(init_pos-list[0])
    for index in range(1,len(list)):
		sum = sum + abs(list[index-1]-list[index])
        
    return(list,sum,direction)

def get_pf(list):
    "returns list of page faults and default list without them"
    list_pf=[]
    for i in range(len(list)-1,-1,-1): # recorremos en forma inversa para no perer indices
        if list[i] < 0:
            list_pf.append(abs(list.pop(i)))
    list_pf.reverse()
    return list_pf

def attend_pf(list,init_pos,direction):
    pf_list = get_pf(list)
    return fifo(pf_list,init_pos, direction)

# FCFS  implementation
def FCFS(list,init_pos,direction):
    pf_result = attend_pf(list,init_pos,direction)
    print pf_result
    print list
    count=pf_result[1]
    fifo_result = fifo(list,pf_result[0][-1],pf_result[2])
    count += fifo_result[1]
    print pf_result[0]
    print fifo_result[0]
    listatendida = pf_result[0].extend(fifo_result[0])
    print listatendida
    return (fifo_result[1],fifo_result[2])

#def SSTF():
 #   atender pfs
  #  
   # hacer copia lista orig
    #mientras elem
    #    obtener prox
     #   elim de listay append 

   ## sacar lista distancias
    #obtener minimo e indice (lista distancias) 

# # Data conversor

###########     TESTS
#print "testeando fifo"
#lachota = [200,150,400,35]
#tupla = fifo(lachota, 100, True)
#print tupla
#print "fin test fifo"

#print "test get_pf"
# l=random_list(10)
# add_random_pf(l,3)
# pfss=get_pf(l)
# print pfss

print "test FCFS"
lfcfs=[399,190,120,-450,350,511,-12,-130,510,150]
print FCFS(lfcfs,1,False)


print "end test FCFS"
