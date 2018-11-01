# Problem 5:
def replaceAll(astring,lookfor,replaceWith):
    rstring = ""
    while astring.find(lookfor) != -1:
        rstring = rstring + astring[:astring.find(lookfor)] + replaceWith
        astring = astring[astring.find(lookfor) + len(lookfor):]
    rstring = rstring + astring
    return rstring
# Test results:

print(replaceAll('whatever, what','what','where'))
# returns 'whereever, where'

print(replaceAll('he said, she said','he','she'))
# returns 'she said, sshe said'

print(replaceAll('he said whatever else','whatever',' '))
# returns 'he said   else"

# Problem 6:
def countWords(s):
    return len(s.split())