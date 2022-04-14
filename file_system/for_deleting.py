import os
#os.remove("a.txt")
if os.path.exists("a.txt"):
    os.remove("a.txt")
else:
    print("file does not exist")