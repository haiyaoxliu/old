# language implementation

# original

def space(string):
    #init tokens with empty if it doesnt exist
    tokens = []
    short = ''.join(string.split())
    for i in range(len(short)):
        if i.isnumeric():
            tokens.append(short[i])
        if i == '(':
            space(short)
        if i == ')':
            continue

def convert(string):
    tokens = []
    split = ''.join(string.split())
    for i in range(len(split)):
        #print(tokens)
        #print(split)
        if split[i].isnumeric():
            try:
                if split[i-1].isnumeric():
                    tokens[-1] += split[i]
                    #tokens[-1][1] += split[i]
                else:
                    tokens.append(split[i])
                    #tokens.append(['n',split[i]])
            except IndexError:
                tokens.append(split[i])
                #tokens.append(['n',split[i]])
        elif split[i] == '(':
            #print(split[i+1:])
            p = convert(''.join(split[i+1:]))
            #print(p[0])
            tokens.append(p[0])
            i = i + p[1] + 1
            continue
        elif split[i] == ')':
            print(tokens)
            print(i)
            return [tokens,i]
        else:
            tokens.append(split[i])
    print(tokens)

def chew(string):
    tokens = ['']
    cut = ''.join(string.split())
    for i in cut:
        pointer = i
        print(cut)
        if pointer.isnumeric():
            if tokens[-1].isnumeric():
                tokens[-1] += i
            else:
                tokens.append(i)
    print(tokens)
#chew(" 403tger09i0vfs-9he  9 8rhs9vea sefa9pwf983w8   ")
#convert('55   *(  1 + (442 + 3)  )*        3')

def tokenize(string):
    tokens = ['init']
    expr = ''.join(string.split())
    for i in expr:
        if i.isnumeric() and tokens[-1].isnumeric():
            tokens[-1] += i
        else:
            tokens.append(i)
    return tokens[1:]

#sample_expression = tokenize("10*((10 + 1) / 1 - 2) / 3 + 5     * 0")
#print(sample_expression)

def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

bop = {'*':mult,'/':div,'+':add,'-':sub}

def p(tokens,expr):
    #print(expr)
    if len(tokens) == 0:
        return expr
    c = tokens[0]
    del tokens[0]
    if c.isnumeric():
        #expr = '|num {} |'.format(c)
        expr.append(['num',c])
    elif c in bop:
        #expr += '|op {} |'.format(c)
        expr.append(['op',c])
    elif c == '(':
        #expr += ' (subexpr '
        sub = p(tokens,[])
        expr.append(['subexpr', sub[1]])
        tokens = sub[0]
    elif c == ')':
        #expr += ' endsubexpr)'
        return [tokens, expr]
    else:
        return 'error'
    return p(tokens,expr)

def VAL(token):
    #print(token)
    #print(token[1])
    return token[1]

def TYPE(token):
    return token[0]

def test(expr,op):
    ref = {'sum':'+-','prod':'*/','exp':'^'}
    for i in range(len(expr)):
        if type(VAL(expr[i])) is str:
            if VAL(expr[i]) in ref[op]:
                #print(expr[i])
                return i
    return False

def tree(expr):
    root = []
    #print(expr)
    if len(expr) == 1:
        if TYPE(expr[0]) == 'num':
            return VAL(expr[0])
        elif TYPE(expr[0]) == 'subexpr':
            return tree(VAL(expr[0]))
        else:
            print('atom level error')
            return
    else:
        s = test(expr,'sum')
        p = test(expr,'prod')
        if s:
            root = [VAL(expr[s]), tree(expr[:s]), tree(expr[s+1:])]
            return root
        elif p:
            root = [VAL(expr[p]), tree(expr[:p]), tree(expr[p+1:])]
        else:
            return 'operation search error'
    return root

#print(tree(p(tokenize('(0)'),[])))
def testcases():
    trials = ['(0)','1+2','3-4','5*6','7/8','(9+10)','11+(12-13)','14+(15-(16*(17/18+(19))))']
    results = [tree(p(tokenize(exp),[])) for exp in trials]
    for i in results:
        print('result: '+str(evaluate(i)))
        print('\n')

def evaluate(tree):
    #print('eval:')
    print(tree)
    if type(tree) == str:
        if tree.isnumeric():
            return int(tree)
        else:
            return 'error bad #'
    elif len(tree) == 1:
        if type(tree[0]) == list:
            return evaluate(VAL(tree[0]))
        else:
            return 'error bad subexpr'
    elif len(tree) == 3:
        if tree[0] in bop:
            return bop[tree[0]](evaluate(tree[1]),evaluate(tree[2]))
        else:
            return 'error invalid tree inside'
    else:
        return 'error invalid tree'

testcases()

def testrun():
    i = ''
    print('\n\n\ntype expression to evaluate, "quit" to quit')
    while True:
        i = input('expression: ')
        if ''.join(i.split()) == 'quit':
            print('quitting')
            return
        print('result: ' + str(evaluate(tree(p(tokenize(i),[])))) + '\n')

testrun()

#print(t)
#tree:expr
#   root = [op,e1,e2]
#   if expr is num >return num
#   else try add:expr
#       >root = [ + or -, tree(left), tree(right)]
#   else try mult:expr
#       >root = [ * or /, tree(left), tree(right)]
#   return root
#   (no ^ support)



# translated from js

def parseEXP(program):
    program = strip(program)
    
def strip(string):
    