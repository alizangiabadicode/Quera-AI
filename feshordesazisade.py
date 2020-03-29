reshte = input()
current_char = reshte[0]
times = 0
index= 0
for char in reshte:
    index+=1
    if (char != current_char):
        print(current_char, times, sep="", end="")
        times= 1
        current_char = char
    else:
        times+=1
    if (index == len(reshte)):
        print(current_char, times, sep="", end="")
