#non-regex apcs homework header constructor

#heading format:
#<fname> <lname>
#APCS<s> pd<n>
#HW<n> -- <t>
#<yyyy>-<mm>-<dd>

#homework title search could be better, idk

#info sources:
#date uses strftime from datetime module
#term, hw number, hw title all retrieved from the homework website
#white links behind homework title are not retrieve

#first time use will request name and period number and generate config file storing these in the python file's directory
#after that only filename will be requested. if the filename does not end in .java, it will be automagically appended

import urllib2
import datetime
import os.path

now = datetime.datetime.now()
name = ''
period = ''
path = ''

latest = urllib2.urlopen("https://docs.google.com/a/stuycs.org/document/d/1Bn5-rMMzS7s2s0vuNk3n8YYowFiSuwhmhTaZWGacl1A/pub")
source = latest.read()
#print(source)
def main():
    try:
        config = open('config.txt','r')
        text = config.read().split('\n')
        name = text[0]
        period = text[1]
        path = text[2]
        config.close()
    except:
        name = raw_input('full name: ')
        period = raw_input('period: ')
        path = raw_input('path to create files in: ')
        config = open('config.txt','w')
        config.write(name)
	config.write('\n')
        config.write(period)
        config.close()

    fn = raw_input('filename (java class name): ')
    if (not fn.endswith('.java')):
        fn += '.java'
    hn = source.find('HW #')
    ht = source.find('>: ') + 3

    term = source[source.find('<div id=\"header\">')+17:source.find('<div id=\"header\">') + 22]
    number = source[ source.find('</span>',hn+11) - 2: source.find('</span>',hn+11)]
    title = source[ht:source.find('</span>',ht)]
    date = now.strftime('%Y-%m-%d')

    heading = '//' + name + '\n//' + term + ' pd' + period + '\n//' + 'HW' + number + ' -- ' + title+ '\n//' + date
    
    hwfile = open(fn,'w')
    hwfile.write(heading)
    hwfile.close()

main()