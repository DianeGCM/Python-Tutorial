import turtle

var_1 = turtle.Turtle()

var_1.width(10)         #"width of the turtle pen"
var_1.color("red")      #"color of the turtle pen"
var_1.forward(50)       #"move and write if the pen is down"
var_1.up()
var_1.backward(50)

var_1.left(15)

var_1.color("yellow")
for i in range(10):
 var_1.stamp()
 var_1.forward(10)

var_1.setposition(60,60)
x = var_1.stamp()
var_1.setpos(40,40)

var_1.down()
var_1.color("blue")
var_1.setpos(-80, -40)
var_1.left(45)
var_1.forward(50)

var_1.setpos(-40, 50)
var_1.circle(90)
var_1.clearstamp(x)

var_1.hideturtle()

turtle.done()



