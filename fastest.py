from simulator import Simulator

s = Simulator()
s.init_pos = 0
s.requirements = [-307, 145, 133, 66, 312, -254, -477, 179, 114]
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.init_pos = 0
s.requirements = [-307, 145, 133, 66, 312, -254, -477, 179, 114]
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.init_pos = 511
s.requirements = [307, 145, 133, 66, 312, 254, 477, 179, 114]
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.requirements = [307, 145, 133, 66, 312, 254, 477, 179, 114]
s.init_pos = 0
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"

s = Simulator()
s.requirements = [307, 145, 133, 66, 312, 254, 477, 179, 114]
s.init_pos = 511
print "executeFCFS()", s.executeFCFS(), "end FCFS"
print "executeSSTF()", s.executeSSTF(), "end SSTF"
print "executeCLOOK()", s.executeCLOOK(), "end CLOOK"
print "executeCSCAN()", s.executeCSCAN(), "end CSCAN"
print "executeLOOK()", s.executeLOOK(), "end LOOK"
print "executeSCAN()", s.executeSCAN(), "end SCAN"