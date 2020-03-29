import math
input = input()
input = input[:len(input) -1].split(' ')
temp =[]
for i in input:
    temp.append(int(i))
input = temp
input.sort()
miangin = 0
for i in input:
    miangin += i
miangin = miangin / len(input)
miane = (len(input) - 1) / 2.0
if (int(miane) == miane):
    miane = input[miane]
else:
    miane = (input[math.ceil(miane)] + input[math.floor(miane)]) / 2
dict = {}
for i in input:
    if (dict.get(i) == None):
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
temp = list(dict.values())
temp.sort()
temp = list(dict.values()).index(temp[-1])
mod = list(dict.keys())[temp]
print("%.2f" % miangin)
print("%.2f" % miane)
print(mod)