#Matthew Siegel
#5/4/18
#warmup15.py - doubling a list

def double(L):
    for i in range(0,len(L)):
        L[i] = L[i]*2
    return L
    
print(double([13,3,5,1,7,5,1,23,54,100]))
