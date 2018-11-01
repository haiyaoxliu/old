import turtle
import math

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color

surround = [[-300,-300],[-300,0],[-300,300],[0,300],[300,300],[300,0],[300,-300],[0,-300]]
point = [-50,-50]

def shell(n,length):
    points = []
    myPen.up()
    x = -length/2
    y = -((length)/(2*math.tan(math.pi/n)))
    myPen.goto(x,y)
    myPen.down()
    for i in range(n):
        vertex = myPen.position()
        points.append(vertex)
        myPen.forward(length)
        myPen.left(360/n)
        midpoint = scale(vertex, myPen.position(), 1/2)
        points.append(midpoint)
    #print(points)
    return (points)

def scale(p1, p2, ratio):
    return ( (p1[0] + p2[0]) * ratio, (p1[1] + p2[1]) * ratio)

def carpet(point,size,depth,case,ratio):
    #print(len(case))
    draw(size, point, len(case)/2)
    if depth > 0:
        for i in range(len(case)):
            carpet(scale(point, case[i], ratio), size*ratio, depth - 1, case, ratio)

def draw(size, point, sides):
    myPen.up()
    myPen.goto(point[0], point[1])
    myPen.begin_fill()
    for i in range(int(sides)):
        myPen.forward(size)
        myPen.left(360/sides)
    myPen.end_fill()

carpet([-50,-87],100,2,shell(6,800),1/5)