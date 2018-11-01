# file reading
import re

#text = open('text>list.txt','r')
#cmsplit = []

#for line in text:
#    info = line.split(', ')
#    cmsplit.append(info)
#    line = line.replace('\xe2\x80\x99',"'")
#    info = line.split()
#    translate[info[0]] = " ".join(info[1:])
#print(translate)

#def maxfile(name):
#    txt = open(name,'r')
#    csplit = [re.search(r'[^, \n]', line).group(1) for line in txt]
#    print(csplit)

#maxfile('text>list.txt')

#sent = 'the the hwool. hello world'
#words = re.split(r'[\.,;\s]\s*', sent)
#print words
#for word in words:
#    if word in translate.keys():
        #print(translate[word])
#        sent = sent.replace(word,translate[word])
#print(sent)

def sl(l):
    o = [l[0]]
    for i in range(1,len(l)):
        s = 0
        for j in range(len(o)):
            if l[i] < o[j]:
                o.insert(j,l[i])
                s = 1
                break
        if s == 0:
            o.append(l[i])
    print(o[-2])

sl([9,1,8,2,6,7])