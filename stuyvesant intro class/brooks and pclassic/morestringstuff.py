# classwork

def cv(s):
    v = "aeiouyAEIOUY"
    n = 0
    for i in s:
        if i in v:
            n = n + 1
    return n

print(cv('abcdefghijklmnopqrstuvwxyz facetious ABCDEFGHIJKLMNOPQRSTUVWXYZ FACETIOUS')) # 22
print(cv('aeiouyAEIOUY lots of consonants')) # 17


# additional string stuff

# 1

def countChars(s,c):
    n = 0
    for i in s:
        if i == c:
            n = n + 1
    return n

print(countChars('abcab','b'))  # returns 2
print(countChars('lots of aaaas and bbbbbbbs','a')) # 5


# 2

def howManyOfAinB(alphabet,s):
    n = 0
    for i in alphabet:
        if i in s:
            n = n + 1
    return n

print(howManyOfAinB('aeiou','on the other hand'))  # returns 3 because only 'a', 'e' and 'o' appear inside the string
print(howManyOfAinB('facetious','i finished the homework')) # 6




# challenge problem

def countStrings(s,substring):
    n = 0
    c = 0
    for i in s:
        if i == substring[c]:
            c = c + 1
        else:
            c = 0
        if c >= len(substring):
            n = n + 1
            c = 0
    return n

print(countStrings('on the other hand','the'))  # returns 2
print(countStrings('facetious is a word in which all the vowels in the alphabet appear in order','in')) # 3
print(countStrings('a b a b a b c d e a b a','a')) # 5
print(countStrings('axydkjsbgkjherliugfd;gl[5i96t59u3th2o3unfkfsdg','k')) # 3

