f=open("test.txt","r")
#print(f.read())
#print(f.read(1))
#print(f.readline())
for i in f:
    print(i)
f.close()
