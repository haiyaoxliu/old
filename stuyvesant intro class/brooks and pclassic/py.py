# loopy exercises 

import math

#1 fred(q) = q*q-3
def fred(q):
    return q*q - 3

#2 sumfredwhile, sum freds from 0 to n-1, use while
def sumFredWhile(n):
    sum = 0
    while n > 0:
        sum = sum + fred(n-1)
        n = n - 1
    return sum

#3 sumfredfor, same as 2 except with for
def sumFredFor(n):
    sum = 0
    for i in range (0,n):
        sum = sum + fred(i)
    return sum

#4
def sumFredBetween(low,high):
    return sumFredFor(high) - sumFredFor(low)

#5
def sumFredBetween2(low,high):
    return sumFredBetween(min(low,high),max(low,high))
  
#6  
def factorPairs(n):
    for i in range(1,n/2):
        if n % i == 0 and i*i<=n:
            print(str(i) + " " + str(n/i))
            
# isPrime
def isPrime(n):
    for i in range(2,int(n**.5)+1):
        if n % i == 0: return False
    return True

# largestPrimeFactor
# def largestPrimeFactor(n):
    

print(fred(3))
print(sumFredWhile(3))
print(sumFredFor(3))
print(sumFredBetween(1,4))
print(sumFredBetween2(1,4))
factorPairs(25)
print(isPrime(12345677654381))
print(isPrime(2))
print(isPrime(12345678911))