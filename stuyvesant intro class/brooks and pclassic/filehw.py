# file hw
import re
vowels = 'aeiouAEIOU'
alpha = 'abcdefghijklmnopqrstuvwxyz'

#1
def wc(f):
    text = open(f,'r')
    lines = [line for line in text]
    text.close()
    counts = [len('\n'.join(lines)), len(' '.join(lines).split()), len(lines)]
    return counts

print(wc('fred.txt'))
print(wc('harry.txt'))

#2
def igpay(infile,outfile):
    intext = open(infile,'r')
    file = intext.read()
    intext.close()
    chopped = re.findall(r"[\w']+|[.,!?; \n]", file)
    for i in range(len(chopped)):
        #if chopped[i].isalpha():
        chopped[i] = translate(chopped[i])
    outext = open(outfile,'w')
    outext.truncate()
    outext.write(''.join(chopped))

def translate(word):
    if word[0] in vowels:
        return word + 'way'
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:] + word[:i] + 'ay'
    return word + 'ay'

igpay('fred.txt','edfray.txt')
igpay('sky.txt','test.txt')

#3
def HighLow(file):
    data = open(file,'r')
    grades = {re.split(r'[,\n]', line)[0]:re.split(r'[,\n]', line)[1] for line in data}
    data.close()
    h,l = sorted(grades,key=grades.get)[-2],sorted(grades,key=grades.get)[0]
    print('highest: ' + h + ' with ' + grades[h])
    print('lowest: ' + l + ' with ' + grades[l])
    #print(grades)

HighLow('name_grade.csv')

#4
def Rank(infile,outfile):
    data = open(infile,'r')
    grades = {re.split(r'[,\n]', line)[0]:re.split(r'[,\n]', line)[1] for line in data}
    data.close()
    #print(grades)
    ranked = '\n'.join([i + ',' + grades[i] for i in sorted(grades,key=grades.get,reverse=True)])
    ranks = open(outfile,'w')
    ranks.truncate()
    ranks.write(ranked)
    ranks.close()

Rank('name_grade.csv','re-ranked.csv')

#5
def CharRank(file):
    data = open(file,'r')
    chars = ''.join(filter(str.isalpha, data.read())).lower()
    data.close()
    nums = {n:chars.count(n) for n in alpha}
    schars = [i for i in sorted(nums,key=nums.get,reverse=True) if nums[i] != 0]
    #print(nums)
    return ''.join(schars)
    
print(CharRank('harry.txt'))
print(CharRank('englishwords.txt'))
print(CharRank('BillOfRights.txt'))

