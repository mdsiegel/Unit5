#Matthew Siegel
#4/25/18
#warmup13.py-list of random nums
from random import randint

L = []
for i in range(0,20):
    L.append(randint(1,100))
count = 0
for i in range(0,len(L)):
    count+=L[i]
print(count)

max = 0
for i in range(0,len(L)):
    if L[i]>max:
        max = L[i]
print(max)

min = 100
for i in range(0,len(L)):
    if L[i]<min:
        min = L[i]
print(min)

