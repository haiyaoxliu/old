dic = open('dict.txt','r')
translate = {}
for line in dic:
    line = line.replace('\xe2\x80\x99',"'")
    info = line.split()
    translate[info[0]] = " ".join(info[1:])
    
#print(translate)
import re
sent = 'the the hwool. hello world'
words = re.split(r'[\.,;\s]\s*', sent)
#print words
for word in words:
    if word in translate.keys():
        #print(translate[word])
        sent = sent.replace(word,translate[word])
print(sent)