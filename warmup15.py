#Matthew Siegel
#5/4/18
#warmup15.py - doubling a list

def double(L):
    for i in range(0,len(L)):
        L[i] = L[i]*2
    return L
    
print(double([1,2,3]))
