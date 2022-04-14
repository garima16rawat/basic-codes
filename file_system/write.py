f=open("test.txt","w")
f.write("all family members are  doing good")
f.close()

f=open("test.txt","r")
print(f.read())
f.close()