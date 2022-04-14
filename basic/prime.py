num,mum=int(input("enter any number").split())
if num>1:
 for i in range(2,int(num/2+1)):
  if (num%i)==0:
   print(num,"is not a prime number")
   break
 else:
        print(num,"is a prime number")
else:
 print("i am not aprime number")


