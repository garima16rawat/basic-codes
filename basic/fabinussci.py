num=int(input("enter number: "))
n1,n2=0,1
count=0
if num<=0:
    print("enter positive number")
elif num==1:
    print(n2)
else:
    while count < num:
     print(n1)
     nth = n1 + n2
     n1 = n2
     n2 = nth
     count += 1




