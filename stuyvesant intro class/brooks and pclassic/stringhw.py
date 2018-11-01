# string exercises homework

# 1A

def ToUpper(s):
    uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lc = "abcdefghijklmnopwrstuvwxyz"
    for i in range(len(lc)):
        s = s.replace(lc[i], uc[i])
    return s

print(ToUpper("Mxa2 [e}fs a'BcD"))

#-----------------------------------#

def upc(s):
    return convertinplace(s,"abcdefghijklmnopwrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def lwc(s):
    return convertinplace(s,"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopwrstuvwxyz")

# general functions                 #
def convertinplace(s,b,a):
    for i in range(len(b)):
        s = s.replace(b[i], a[i])
    return s
    
def convertc(s, b, a):
    n = ""
    for i in range(len(s)):
        if b.find(s[i]) != -1:
            n = n + a[b.find(s[i])]
        else: n = n + s[i]
    return n
    
#def value(s): convert to value for comparisons
#-----------------------------------#

# 1B

def Encrypt(s):
    return convertc(s, 'defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def Decrypt(s):
    return convertc(s, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC')

print(Encrypt("This is just a sentence. And then some test chars: 12#$[}|\~` "))
print(Decrypt(Encrypt("This is just a sentence. And then some test chars: 12#$[}|\~` ")))

#2a

def IsSameName(s,t):
    return upc(s) == upc(t)
    
print(IsSameName('John smith', 'JOHN Smith')) # returns True
print(IsSameName('John Smith', "John's Myth"))  # returns False

#2b

def CapWord(w):
    return upc(w[0]) + lwc(w[1:])

print(CapWord('joHN'))  # returns 'John Smith'

#2c

def CapName(n):
    return CapWord(n.split()[0]) + " " + CapWord(n.split()[1])

print(CapName('joHN SMith'))  # returns 'John Smith'

#3a

def FirstLast(n):
    return n.split(', ')[1] + ' ' + n.split(', ')[0]

print(FirstLast('Brooks, Peter'))  # returns 'Peter Brooks'

#3b

def FirstLastSequence(n):
    l = n.split(';')
    del l[-1]
    s = ""
    for i in l:
        s = s + FirstLast(i) + ";"
    return s

print(FirstLastSequence('Brooks, Peter;Holmes, David;Pascu, Ms.;')) # returns 'Peter Brooks;David Holmes;Ms. Pascu;'

#4

def FileClassifier(n):
    l = {'jpg':'picture', 'jpeg':'picture', 'mp3':'music', 'nlogo':'Netlogo', 'py':'Python'}
    return l[lwc(n.split('.')[-1])]

print(FileClassifier('StarSpangledBanner.Mp3'))  # returns 'music'
print(FileClassifier('Fred.mp3.JPEG.nlogo'))     # returns 'Netlogo'2

# 3/23/16 Classwork
def findfred(s):
    u = upc(s)
    return s[ s.rfind(',', 0, u.find('.JPG')) + 1 : u.find('.JPG') + 4 ]
    
print(findfred("abc,75jgggjklll def.hj,fred.jpg,xym21 44#4.llk&*07-"))