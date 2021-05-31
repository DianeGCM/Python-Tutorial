import turtle

var_1 = turtle.Turtle()

var_1.width(10)         #"width of the turtle pen"
var_1.color("red")      #"color of the turtle pen"
var_1.forward(50)       #"move and write if the pen is down"
var_1.up()
var_1.backward(50)

var_1.left(15)          #move the pen 15 deg counter clockwise

var_1.color("yellow")
for i in range(10):
 var_1.stamp()          #stamp the pen and  -  Notice the stamp command does not need the pen to be down in order to "stamp" the screen
 var_1.forward(10)       #move the pen forward

var_1.setposition(60,60)   #move the turtle to a different location
x = var_1.stamp()           #we used a variable x to note the stamp number. Each stamp has a number and can be deleted.

var_1.setpos(40,40)     #move the turtle to another location 
var_1.down()            #put the pen down
var_1.color("blue")       
var_1.setpos(-80, -40)   #when we jumped to another location, the turtle drew a line from location (40,40)  to location (-80, -40)   

var_1.circle(90)         #create a circle with a diameter of 90
var_1.clearstamp(x)      #deletes the last stamp that we drew

var_1.hideturtle()        #hides the turtle (cursor)

turtle.done()



