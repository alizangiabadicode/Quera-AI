username = input()
password = input()
name , age , bmi = input().split()
print("<user>")
print("\t<combo>", username, ":", password, "</combo>", sep= '')
print("\t<name>", name, "</name>", sep= '')
print("\t<age>", age, "</age>", sep= '')
print("\t<bmi>", "%.3f"%float(bmi), "</bmi>", sep= '')
print("</user>")



# print(txt_1, txt_2, ... , txt_n,end='\n',sep=' ',file=sys.stdout,flush=True)
# #print function signature and it's default options