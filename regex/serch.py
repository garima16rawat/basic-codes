import re
text="i am a string"
x=re.search("\s",text)
print("the first white space is",x.start())
y=re.split("\s",text,1)
print(y)
z=re.sub("\s","9",text)
print(z)