#Matthew Siegel
#5/7/18
#quiz5.py - list quiz

def penultimate(A):
    return A[-2]
    
def plusEquals(B,C):
    for number in B:
        number +=C
    return B

print(penultimate([3,4,5,6,7]))
print(plusEquals([1,2,3,4],10))



