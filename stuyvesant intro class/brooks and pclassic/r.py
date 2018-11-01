#! /usr/bin/python
# Show variables passed via CGI

import cgi
import cgitb
cgitb.enable()

def parse():
    form=cgi.FieldStorage()
    the_keys=form.keys()
    the_keys.sort()
    html=''
    for akey in the_keys:
        avalue=form.getvalue(akey,'')
        html+=akey+'='+str(avalue)+'<br>\n'
    print 'Content-type: text/html\n'
    print '<html><body><b>Variables and values sent:</b><p>\n'
    print html
    print '</body></html>'

parse()

#print 'Content-type: text/html\n'
#print '<html><body><b>Variables and values sent:</b><p>\n'
#print 'test success'
#print '</body></html>'


