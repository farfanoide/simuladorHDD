from simulator import Simulator

s = Simulator()
s.init_pos = 0
s.requirements = [-307, 145, 133, 66, 312, -254, -477, 179, 114]

print s.executeFCFS()
print s.executeSSTF()
print s.executeCLOOK()
print s.executeCSCAN()
print s.executeLOOK()
print s.executeSCAN()
s.requirements = [307, 145, 133, 66, 312, 254, 477, 179, 114]

print s.executeFCFS()
print s.executeSSTF()
print s.executeCLOOK()
print s.executeCSCAN()
print s.executeLOOK()
print s.executeSCAN()