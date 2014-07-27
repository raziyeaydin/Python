import turtle

t=turtle.Turtle()
  
def cember(yaricap, aci):
    
    renkler = ("orange", "yellow", "red")
    
    for renk in renkler:
        t.color(renk)
        t.begin_fill()
        t.forward(yaricap)
        t.left(90)
        t.circle(yaricap, aci)
        t.left(90)
        t.forward(yaricap)
        t.left(180)
        t.end_fill()
        

    t.color("white")
    t.pensize(5)
    for i in range(3):
        t.fd(yaricap)
        t.bk(yaricap)
        t.lt(aci)

cember(300,120)

t.up()
t.goto(0,-200)
t.down()
t.begin_fill()
t.circle(200)
t.end_fill()

t.pensize(1)

t.up()
t.goto(-300,0)
t.down()

def ozgurluk (yaricap, renk1, renk2):
    t.color(renk1)
    t.fill(True)
    t.circle(yaricap/2.0, 180)
    t.circle(yaricap, 180)
    t.left(180)
    t.circle(-yaricap/2.0, 180)
    t.fill(False)
    t.color(renk2)
    t.left(90)
    t.up()
    t.forward(yaricap/2.0)
    t.dot(yaricap/4.0)
    t.back(yaricap/2.0)
    t.down()
    t.left(90)

ozgurluk (60, "yellow" , "orange")
ozgurluk (60, "orange" , "yellow")
t.color("white")
t.up()
t.forward(60)
t.down()
t.left(90)
t.pensize(5)
t.circle(60)

t.pensize(1)
t.up()
t.goto(212,212)
t.down()
ozgurluk (60, "red" , "orange")
ozgurluk (60, "orange" , "red")
t.color("white")
t.up()
t.forward(60)
t.down()
t.left(90)
t.pensize(5)
t.circle(60)

t.pensize(1)
t.up()
t.goto(212,-212)
t.down()
ozgurluk (60, "red" , "yellow")
ozgurluk (60, "yellow" , "red")
t.up()
t.forward(60)
t.down()
t.left(90)
t.color("white")
t.pensize(5)
t.circle(60)

t.up()
t.home()
t.down()
t.color("black")
t.ht()
t.write("Linux for human beings")

import time
time.sleep(3)



