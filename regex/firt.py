import re
text="I am a python developer"
x=re.search("^I.*developer$",text)
if x:
    print("yes,we have a mutch")
else:
    print("no match")
y=re.findall("p",text)
print(y)