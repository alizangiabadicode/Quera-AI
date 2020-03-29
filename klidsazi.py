input = input()
s = 0
temp = input[0].lower()
c=1
output=""
for char in input:
    if temp == char.lower():
        s+= c*(ord(char) - 64)
        c+=1
    else:
        output = output + str(s)
        c = 2
        temp = char.lower()
        s=ord(char) - 64
output = output + str(s)
print(output)