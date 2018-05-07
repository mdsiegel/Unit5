#Matthew Siegel
#5/7/18
#quiz5.py - list quiz

def penultimate(A):
    return A[-2]
    
def plusEquals(B,C):
    for i in range(0,len(B)):
        B[i] += C
    return B

def smallest(D):
    small = sum(D)
    for number in D:
        if number < small:
            small = number
    return small

print(penultimate([3,4,5,6,7]))
print(plusEquals([1,2,3,4],10))
print(smallest([11,2,3,4]))

