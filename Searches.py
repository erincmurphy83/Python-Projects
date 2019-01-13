from random import randrange
from time import time

def make_random_list(n):
    l = []
    for i in range(n):
        l.append(randrange(n*n))
    return l

def linear_search(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i
    return -1

def binary_search(l, x):
    low = 0
    high = len(l)- 1
    while low <= high:        
        mid = (low + high)//2
        item = l[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1
    
def main():
    l = make_random_list(1000000)
    t1 = time()
    pos = linear_search(l, 555)
    t2 = time()
    if pos != -1:
        print("Linear search found 555 at position", pos)
        print("Time for search =", t2-t1)
        l.sort()
        t1 = time()
        pos = binary_search(l, 555)
        t2 = time()
        print("Binary search found 555 at position", pos)
        print("Time for search =", t2-t1)

main()
