 
 
#f=open("my.txt","x") 
f=open("my.txt","w")
f.write("i am a new")
f.close()
f=open("my.txt","r")
print(f.read())
f.close()

f=open("my.txt","a")
f.write("wellcome")
f.close()
f=open("my.txt","r")
print(f.read())
f.close()