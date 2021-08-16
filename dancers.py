"""
This project was taken from python turtle demos
and was modified to make it understandable for python beginners.

Dancing turtles have a compound shape
consisting of a series of triangles of
decreasing size.

Turtles march along a circle while rotating
pairwise in opposite direction, with one
exception. Does that breaking of symmetry
enhance the attractiveness of the example?

Press any key to stop the animation.

Technically: demonstrates use of compound
shapes, transformation of shapes as well as
cloning turtles. The animation is
controlled through update().
"""

import turtle

global running

def stop():
    global running
    running = False

sh = turtle.Shape("compound")
win_ = turtle.Screen()
win_.clearscreen()
win_.bgcolor("gray10")
win_.tracer(False)
    
turtle.shape("triangle")
f =   0.793402
phi = 9.064678
s = 5
c = 1
turtle.hideturtle()

    # create compound shape
for i in range(10):
        turtle.shapesize(s)
        p = turtle.get_shapepoly()
        s *= f
        c *= f
        turtle.tilt(-phi)
        sh.addcomponent(p, (c, 0.25, 1-c), "black")
turtle.register_shape("multitri", sh)
    
    
    # create dancers
dancer=turtle.Turtle()
dancer.shapesize(1)
dancer.shape("multitri")
dancer.pu()
dancer.setpos(0, -200)
dancers = []

for i in range(180):
        dancer.fd(7)
        dancer.tilt(-4)
        dancer.lt(2)
        win_.update()
        if i % 12 == 0:
            dancers.append(dancer.clone())   #dancers in the list are clones

dancer.home()

    # dance
running = True
win_.onkeypress(stop)
win_.listen()
cs = 1

while running:
        
#      move the clone dancers:
        for l in range(0, len(dancers), 1):     
            dancers[l].fd(7)
            dancers[l].lt(2)
            dancers[l].tilt(-4)

            #move and enlarge the dancer in the center
        if cs < 180:
            dancer.right(4)
            dancer.shapesize(cs)
            cs *= 1.005     
        else:
            cs = 1    #start all over again

        win_.update()
