def lv(dic):
    return [dic[i] for i in dic]

n = {'a':2, 'p':28, 'z':2, 'm':7, 'y':40, 'f':17, 'g':17, 'h':17, 'k':5}

lv(n)

#invert dict

def inv(dic):
    vals = sorted(dic, key = dic.get)
    keys = sorted(lv(dic))
    inverted = {i:[vals[n] for n in range(len(vals)) if keys[n] == i] for i in set(keys)}
    print(inverted)

#inv(n)



#homework

#1
def readSAT(fn):
    f = open(fn, 'r')
    #ls = [line for line in f]
    d = f.read()
    f.close()
    ls = d.split('\n')
    #print ls
    nls = []
    for l in ls:
        nl = ['']
        i = 0
        while i < len(l):
            if l[i] == ',':
                nl.append('')
            elif l[i] == '"':
                e = l.find('"',i+1)
                nl[-1] += l[i+1:e-1]
                i = e
            elif l[i] == '#':
                return nls[1:]
            elif l[i] == ' ' and l[i+1] == ',':
                pass
            else:
                nl[-1] += l[i]
            i += 1
        for i in range(len(nl)):
            if nl[i].isdigit():
                nl[i] = int(nl[i])
        #print(nl)
        nls.append(nl)
    return nls[1:]
    
#print(readSAT('SAT-2010.csv'))

#2
def HighLowSAT(fn):
    data = readSAT(fn)
    ms = [sd[4] for sd in data if type(sd[4]) == int]
    h = max(ms)
    l = min(ms)
    for i in data:
        if i[4] == h:
            print i[1] + ' has the highest math score, ' + str(i[4])
        if i[4] == l:
            print i[1] + ' has the lowest math score, ' + str(i[4])

HighLowSAT('SAT-2010.csv')

#3
def BigStats(fn):
    data = readSAT(fn)
    ts = 0
    rs = 0
    ms = 0
    ws = 0
    for i in data:
        if type(i[2]) == int and type(i[3]) == int and type(i[4]) == int and type(i[5]) == int:
            ts += i[2]
            rs += i[2]*i[3]
            ms += i[2]*i[4]
            ws += i[2]*i[5]
    print(ts)
    print(float(rs)/ts)
    print(float(ms)/ts)
    print(float(ws)/ts)
    
BigStats('SAT-2010.csv')

#4

def School2Dict(l):
    nl = ['']
    i = 0
    while i < len(l):
        if l[i] == ',':
            nl.append('')
        elif l[i] == '"':
            e = l.find('"',i+1)
            nl[-1] += l[i+1:e-1]
            i = e
        elif l[i] == ' ' and l[i+1] == ',':
            pass
        else:
            nl[-1] += l[i]
        i += 1
    for i in range(len(nl)):
        if nl[i].isdigit():
            nl[i] = int(nl[i])
    return {'DBN':nl[0],'Name':nl[1],'Number':nl[2],'Reading':nl[3],'Math':nl[4],'Writing':nl[5]}

print(School2Dict('01M539,"New Explorations into Sci, Tech and Math HS ",47,568,583,568'))


#5 master dict
def grab(file):
    data = open(file, 'r')
    text = data.read()
    data.close()
    lines = [line.split(',') for line in text.split('\n')]
    headers = lines[0]
    lines = lines[1:]
    #print headers
    #print lines
    people = {line[0]:{headers[h]:line[h] for h in range(len(headers))} for line in lines}
    #for i in people:
    #    print(i + ": " + str(people[i]))
    return people

m = grab('testdata.csv')
print m['F2']['Age']

def something():
    while True:
        x = raw_input('school DBN: ')
        if x not in m:
            print 'invalid DBN'
        else:
            break
    while True:
        y = raw_input('info to get: ')
        if y not in m[x]:
            print 'invalid SAT info'
        else:
            break
    print(str(m[x]['Name']) + "'s " + y + ' is ' + m[x][y])

#something()

#6 ratings search and sort
def persons(file):
    data = open(file, 'r')
    text = data.read()
    data.close()
    lines = [line.split(',') for line in text.split('\n')]
    headers = lines[0]
    lines = lines[1:]
    #print headers
    #print lines
    people = [{headers[h]:line[h] for h in range(len(headers))} for line in lines]
    #for i in people:
    #    print(i + ": " + str(people[i]))
    return people

import operator

def search(file):
    people = persons(file)
    #print(people)
    while True:
        get = raw_input('search string: ').upper()
        if not get.isalpha():
            if get == '0':
                break
            print 'Not a name!'
        else:
            lnames = [person for person in people if person['lname'].startswith(get)]
            fnames = [person for person in people if person['fname'].startswith(get)]
            lnames = sorted(lnames, key = operator.itemgetter('lname'))
            fnames = sorted(fnames, key = operator.itemgetter('fname'))
            for i in fnames:
                print i['fname'] + ' ' + i['lname'] + ' has a rating of ' + i['rating']
            for i in lnames:
                print i['fname'] + ' ' + i['lname'] + ' has a rating of ' + i['rating']
search('p8.csv')
