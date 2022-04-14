n=int(input("enter number: "))
s=0
for i in range(n+1):
    cube=i*i*i
    s+=cube
print(s)