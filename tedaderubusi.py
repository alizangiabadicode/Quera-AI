import sys
input = sys.stdin.readlines()
def findBuses(bus):
    s = 1
    for i in range(-(bus[0]), -1):
        s += s * (-i)
    return s
people = int(input[0].strip())
bus = {}
for i in range(1, len(input)):
    if (bus.get(input[i].strip()) == None):
        bus[input[i].strip()] = [1, 0]
        print(0)
    else:
        bus[input[i].strip()] = [bus[input[i].strip()][0]+1, findBuses(bus[input[i].strip()]) + bus[input[i].strip()][1]]
        print(bus[input[i].strip()][1])