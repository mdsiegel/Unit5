#Matthew Siegel
#5/3/18
#mySort.py - making a sort

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def mySort(A):
    if len(A)<= 1:
        return A
    left = []
    right = []
    for i in range(0,len(A)):
        if i<len(A)/2:
            left.append(A[i])
        else:
            right.append(A[i])
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    while len(left) > 0:
        result.append(left[0])
        left.remove(left[0])
    while len(right) > 0:
        result.append(right[0])
        right.remove(right[0])
    return result

if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
