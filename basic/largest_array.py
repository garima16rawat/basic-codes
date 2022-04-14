l=[23,45,67,43,68]
#print(max(l))
max=l[0]
for i in range(len(l)):
    if l[i] > max:
        max=l[i]
print(max)
