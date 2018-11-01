# List and String exercises
import math
import random

#1

def Esrever(L):
    return [i[::-1] for i in L]
    
Esrever(['abcd','derF'])  # returns ['dcba', 'Fred']
Esrever(['123','!@#,?'])  # returns ['321', '?,#@!']

#2

def RandTest(low,high,numTrials):
    r = [random.randint(low,high) for i in range(numTrials + 1)]
    t = [float(r.count(i))/numTrials for i in range(low,high + 1)]
    return t

print RandTest(11,20,10000)

#3

def Av(l):
    n = [i for i in l if type(i) == int or type(i) == float]
    if len(n) == 0:
        return 0
    return sum(n)/float(len(n))
    
print(Av([3.5, 'Fred', 4.5, 1]))  # returns 3.0
print(Av(range(1,5)))  # returns 2.5

#4

def SmallestPos(L):
    return L.index(min(L))
    
print(SmallestPos([3, 1, -3, 10, 2, 45.04]))  # returns 2, because -3 is the smallest number
print(SmallestPos([12, 3.8, 13, 3.8]))  # returns 1

#5

def SortNums(L):
    s = []
    for i in range(len(L)):
        s.append(L[SmallestPos(L)])
        del(L[SmallestPos(L)])
    return s
    
print(SortNums([7, -3.4, 12, 7, 1.3]))  # returns [-3.4, 1.3, 7, 7, 12]