# ------------------- #
# RECURSION EXERCISES #
# ------------------- #

# 1 --------------------------

def fac(n):
  if n == 1: return 1
  n = n * fac(n-1)
  return n

print(fac(6))

# 2 --------------------------

def rev(l):
  if len(l) == 1:
    return l
  return [l[-1]] + rev(l[0:-1])

print(rev([1,2,3,4,5,6,7]))

# 3 --------------------------



# 4 --------------------------



# 5 Fibonacci ----------------

def fib(n):
  if n < 3: return 1
  return fib(n-1) + fib(n-2)

for i in range(1,20): print(fib(i))

# 6 Hanoi

# Hilbert --------------------

import sys
import turtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'FA++FA++FA'   # Rule 1
    elif ch == 'A':
        newstr = 'A-FA++FA-FA'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    sys.setExecutionLimit(360000)
    inst = createLSystem(4, "X")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 10)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()


# Koch ----------------------------------------

import sys
import turtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F+'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    sys.setExecutionLimit(360000)
    inst = createLSystem(6, "F")   # create the string
    #print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(0)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()

# Pascal -----------------------------------------------------

def pascal(n):
    if n == 0:
        #print([])
        return []
    elif n == 1:
        #print([1])
        return [[1]]
    else:
        new_row = [1]
        result = pascal(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
        #print(result[n-1])
    return result

def row(n):
  print(pascal(n)[n-1])
  
row(6)

# ------------------- #
# Iteration EXERCISES #
# ------------------- #

# 1 --------------------------

import math

def nroot(n,d,t):
  r = n
  while int(10**d*r) != int(10**d*math.sqrt(n)) and t > 0:
    r = (r + n/r)/2
    t = t - 1
    print(int(10**d*r)/10**d)

nroot(2,3,100)

# 2 --------------------------

def tri(n):
  num = 0
  for i in range(n):
    num = num + i
    print(i, num)
    
tri(7)

# 3 --------------------------

import math

def isprime(n):
  for i in range(2,int(math.sqrt(n))+1):
    print(i)
    if n % i == 0:
      return 'no'
  return 'yes'

print(isprime(111))

# 4 --------------------------

import random
import turtle

def isInScreen(w,t):
    hBound = w.window_width() / 2
    vBound = w.window_height() / 2
    turtleX = abs(t.xcor())
    turtleY = abs(t.ycor())

    stillIn = True
    if turtleX > hBound:
        stillIn = False
    if turtleY > vBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
t.speed(0)
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(random.randrange(0,180))
    else:
        t.right(random.randrange(0,180))

    t.forward(50)

wn.exitonclick()

# 5 -----------------------------------

import random
import turtle

def isInScreen(w,t):
    hBound = w.window_width() / 2
    vBound = w.window_height() / 2
    turtleX = abs(t.xcor())
    turtleY = abs(t.ycor())

    stillIn = True
    if turtleX > hBound:
        stillIn = False
    if turtleY > vBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
r = turtle.Turtle()
t.speed(0)
r.speed(0)
#t.goto(random.randrange(-10,10),random.randrange(-10,10))
#r.goto(random.randrange(-10,10),random.randrange(-10,10))
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t) and isInScreen(wn,r):
  coin = random.randrange(0, 4)
  if coin == 0:
    t.left(90)
    r.left(90)
  if coin == 1:
    t.right(90)
    r.left(90)
  if coin == 2:
    t.right(90)
    r.left(90)
  if coin == 3:
    t.right(90)
    r.right(90)
  
  t.forward(50)
  r.forward(50)

wn.exitonclick()

# 6 -------------------------------------

import random
import turtle

def isInScreen(w,t):
    hBound = w.window_width() / 2
    vBound = w.window_height() / 2
    turtleX = abs(t.xcor())
    turtleY = abs(t.ycor())

    stillIn = True
    if turtleX > hBound:
        stillIn = False
    if turtleY > vBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
r = turtle.Turtle()
t.speed(0)
r.speed(0)
t.up()
r.up()
#t.goto(random.randrange(-50,50),random.randrange(-50,50))
#r.goto(random.randrange(-50,50),random.randrange(-50,50))
t.goto(-50,-50)
r.goto(50,50)
t.down()
r.down()
wn = turtle.Screen()
x = 500
t.shape('turtle')
while x > 0: # isInScreen(wn,t) and isInScreen(wn,r)
  x = x - 1
  if abs(t.position()[0]) >= wn.window_width() / 2 or abs(t.position()[1]) >= wn.window_height() / 2:
      t.forward(-50)
  if abs(r.position()[0]) >= wn.window_width() / 2 or abs(r.position()[1]) >= wn.window_height() / 2:
      r.forward(-50)
  if t.position() == r.position():
    #t.left(180)
    #r.reft(180)
    t.forward(-100)
    r.forward(-100)
  coin = random.randrange(0, 4)
  if coin == 0:
    t.left(90)
    r.left(90)
  if coin == 1:
    t.right(90)
    r.left(90)
  if coin == 2:
    t.right(90)
    r.left(90)
  if coin == 3:
    t.right(90)
    r.right(90)
  
  t.forward(50)
  r.forward(50)
  

wn.exitonclick()

# 7 ---------------------------


# ------------------- #
# Read File EXERCISES #
# ------------------- #

s = open("studentdata.txt", "r")
l = s.readline()
while l:
    d = l.split()
    if len(d[1:]) > 6:
        print(d[0])
    l = s.readline()
s.close()

s = open("studentdata.txt", "r")
l = s.readline()
while l:
    d = l.split()
    print(d[0], "\n\tmax: ", max(d[1:]), "\n\tmin: ", min(d[1:]))
    l = s.readline()
s.close()

import turtle
t = turtle.Turtle()
t.speed(0)
wn = turtle.Screen()
i = open('mystery.txt', 'r')
l = i.readline()

while l:
  d = l.split()
  if d[0] == 'UP':
    t.up()
  if d[0] == 'DOWN':
    t.down()
  if len(d) > 1:
    x = int(d[0])
    y = int(d[1])
    t.goto(x,y)
  l = i.readline()
  
wn.exitonclick()

