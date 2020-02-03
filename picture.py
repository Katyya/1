from graph import *
windowSize(1000,900)
canvasSize(1000,900)
brushColor(101,199,208)
rectangle(0,0,1000,400)
"""Sky"""
brushColor(0,0,255)
rectangle(0,400,1000,650)
"""Oceon"""
brushColor(202,208,101)
rectangle(0,650,1000,900)
penColor(202,208,101)
x=0
for i in range(9):
    circle(50+x,680,60)
    x+=200
brushColor(0,0,255)
penColor(0,0,255)
y=0
for i in range(9):
    circle(150+y,610,60)
    y+=200
def sun():
    penColor(255, 243, 67)
    brushColor(255, 243, 67)
    circle(800, 150, 100)
    

def clouds(x,y,r):
    brushColor(255, 255, 255)
    penColor(0, 0, 0)
    penSize(1)
    circle(x , y , r)
    circle(x-r, y+r, r)
    circle(x+r, y, r)
    circle(x , y+r, r)
    circle(x+r, y + r, r)
    circle(x + (2*r), y, r)
    circle(x + ((7 * r)/3), y+r, r)

def sun_unbrella():
    brushColor("Brown")
    penColor(0, 0, 0)
    rectangle(120, 850, 130, 580)
    h=0
    for i in range(5):
        polygon([(125, 580), (30+h, 650), (70+h, 650)])
        h+=40


brushColor("Brown")
penColor(0, 0, 0)
a= circle(250,450,50)
"""задняя часть корабля"""
b=rectangle(250, 450, 450, 500)
"""средняя часть корабля"""
с=polygon ( [(450,450), (540,450), (450,500)] )
"""передняя часть"""
brushColor(0, 0, 255)
penColor(0, 0, 255)
rectangle(200, 400, 1000, 450)
"""вода"""
penColor(0, 0, 0)
brushColor(255,255,255)
penSize(5)
w=circle(480, 465, 10)
"""windows"""
brushColor(0,0,0)
m=rectangle(350, 200, 365, 450)
"""Матча"""
penSize(1)
brushColor(153, 133, 120)
p1=polygon([(365, 200), (450, 325), (390, 325)])
p2=polygon([(365, 450), (450, 325), (390, 325)])
"""парус"""
board=(a,b)
def update():
    if 700 >= xCoord(a):
        moveObjectBy(a, 5, 0)
        moveObjectBy(b, 5, 0)
        moveObjectBy(с, 5, 0)
        moveObjectBy(w, 5, 0)
        moveObjectBy(m, 5, 0)
        moveObjectBy(p1, 5, 0)
        moveObjectBy(p2, 5, 0)

onTimer(update, 50)
sun()
clouds(220,150,30)
clouds(470,100,40)

sun_unbrella()

run()