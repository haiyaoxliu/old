#pclassic 2015??

import math

#1 365-365

def i365():
    c = 0
    a = []
    for i in range(10000000/365,100000000/365):
        if 365*i/10000 == 365*i % 10000:
            c = c + 1
            a.append([365*i,i])
    print str(c) + " matches found"

#i365()

def int365():
    c = 0
    for i in range(10000000,100000000):
        if type(float(i)/365) == int:
            c = c + 1
    print c

#2 piglatin

def pigify(s):
    vowels = "aeiouAEIOU"
    words = s.split()
    platin = [word + 'hay' if word[0] in vowels else word[1:] + word[0] + 'hay' for word in words]
    return ' '.join(platin)

#print(pigify('hello its me'))

#3 Anagrams? 

def anagrams(a,b):
    a = a.lower()
    b = b.lower()
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    la = sorted([chars.find(l) for l in a if l in chars])
    lb = sorted([chars.find(l) for l in b if l in chars])
    return la == lb
    
#print(anagrams("She sells seas shells on the sea shore.", "Shells... SEAS... ShORE. sHE sells ONE th? Sea?!?!!"))
#print(anagrams("She sells seas shells on the sea shore.", "Shells... SEAS... ShORE. sHE sells ONE th? Sea?!?!!s"))

#4 longest substring

def lsub(s):
    s = s.lower()
    l = [0 for i in s]
    c = 0
    for i in range(len(s)):
        if i == len(s)-1 or s[i] != s[i+1]:
            l[c] = l[c] + 1
            c = c + 1
        elif s[i] == s[i+1]:
            l[c] = l[c] + 1
    print(l[0:c])

#lsub("aaabbbbbcc")
#lsub("abbbbbcdddddddd")

#5 nested squares

def lsq(n):
    if n not in range(52):
        return 'error'
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    container = [[i,j] for i in range(n) for j in range(n)]
    print(container)

#lsq(26)

#6 Pascal's Triangle

def pascal(rows):
    container = [[str(int(float(math.factorial(r))/(math.factorial(e)*math.factorial(r - e)))) for e in range(r+1)] for r in range(rows)]
    for i in container:
        print(' '.join(i))
    
#pascal(13)

#3 2013 circular primes

def ip(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        #print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def cp(n):
    n = str(n)
    p = [n[-i:] + n[:-i] for i in range(len(n))]
    for i in p:
        if not ip(int(i)):
            #print 'not prime'
            return False
        else:
            continue
    #print 'all prime'
    return True
    
cp(123456)
cp(113)

#4 2013 sums of digits in bases

def cbase(n,b):
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if n/b == 0:
        return digits[n%b]
    else:
        #print(n%b)
        return str(cbase(n/b,b)) + digits[n%b]

def sdigits(n):
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    s = 0
    for i in n:
        s += digits.index(i)
    return s

def PQpair(n):
    bases = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    sdniab = [[sdigits(b) for b in [cbase(i,b) for b in bases]] for i in range(n+1)]
    print sdniab
    
    # count number of pq pairs for each pair for each element of sdniab (sum digits of ns in all bases) per base pair
    
    pairs = [[bases[i],bases[j]] for i in range(len(bases)) for j in range(i+1,len(bases))]
    print pairs
    counts = []
    for i in pairs:
        sum = 0
        for j in sdniab:
            if j[i[0]] == j[i[1]]:
                sum += 1
        counts.append(sum)
    #ns = [cbase(n,b) for b in bases]
    #sums = [sdigits(i) for i in ns]
    #print ns
    #print sums
    #digits_bases = [[n_digits[d] for d in range(len(n_digits))] for i in bases]
    #print n_digits
    #print digits_bases
    
PQpair(3)
#print(cbase(10,2))
#print(cbase(10,3))
#print(cbase(10,4))
#print(cbase(10,5))