from simulator import Simulator

s = Simulator()
s.init_pos = 0
s.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]
# expected results: 5, 35, 400, 15, 40, 65, 20, 90, 100
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.init_pos = 511
s.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.init_pos = 0
s.requirements = [5, 15, 40, 65, 20, 35, 400, 90, 100]
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.requirements = [5, 15, 40, 65, 20, 35, 400, 90, 100]
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.init_pos = 511
s.requirements = [5, 15, 40, 65, 20, 35, 400, 90, 100]
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"