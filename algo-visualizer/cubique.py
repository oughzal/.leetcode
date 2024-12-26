from functools import reduce
L = []
for n in range(100,1000):
    if n == reduce(lambda s,i : s  + int(i)**3,str(n),0) :
        L.append(n)
print(L)