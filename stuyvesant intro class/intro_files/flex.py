#!/usr/bin/python

import cgi, cgitb

cgitb.enable()

def ExtremeScores_helper(which_column, how_many, is_top):
    f=open('SAT-2010.csv','r')
    s=f.read()
    f.close()
    lines=s.split('\n')
    lines = lines[1:-1]
    field_lists=[]
    for line in lines:
        fields=line.split(',')
        if fields[-1] != 's':
            if '"' not in line:
                field_lists.append(fields)
            else:
                school_name_in_parts = fields[1:-4]
                school_name=','.join(school_name_in_parts)
                school_name=school_name[1:-1]
                new_fields=fields[0:1]+[school_name]+fields[-4:]
                field_lists.append(new_fields)
    list_to_sort=[]
    for f_list in field_lists:
        if 3<=which_column<=5:
            list_to_sort.append([int(f_list[which_column]),f_list[1]])
        else:
            total=int(f_list[3])+int(f_list[4])+int(f_list[5])
            list_to_sort.append([total,f_list[1]])
    if is_top:
        sorted_list=sorted(list_to_sort,reverse=True)
    else:
        sorted_list=sorted(list_to_sort)
    
    return sorted_list[:how_many]

def ExtremeScores(which_column, how_many, is_top):
    the_list=ExtremeScores_helper(which_column, how_many, is_top)
    s=open('SAT-2010.csv','rU').read()
    headers=s.split('\n')[0].split(',')+['Total']
    print(headers[which_column]+' , school')
    for i in range(how_many):
        print(str(the_list[i][0])+' , '+the_list[i][1] + '</br>')

values = cgi.FieldStorage()

print('Content-type: text/html\r\n')
print('<html><body><p><b>Requested Scores:</b></p>\n')
print(ExtremeScores(int(values['stype'].value),int(values['numscores'].value),values['horl'].value))
print('</body></html>')