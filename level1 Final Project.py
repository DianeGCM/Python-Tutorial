import turtle

colors = list(("blue", "green", "red", "brown", "yellow", "white", "black"))

pen = turtle.Turtle()
screen = turtle.Screen()
pen.up()

pen.color("black")
pen.width(5)

#make a filled square function
def square(x, y):
   pen.up()
   pen.goto(x, y)
   pen.down()
   pen.begin_fill() 

   for i in range(4): 
      pen.forward(50)
      pen.left(90)
  
   pen.end_fill()

#draw the color selectors

for x in range(7):
    pen.fillcolor(colors[x])
    square((x*60)+30, 100)


#checks which part of the screen is clicked
#if the color picker is clicked, then the pencolor will selected
#if the shape picker is clicked, then the shape will be selected
#otherwise draw the latest shape/color

def click_check(x, y): 

   if y >= 100 and y < 200: 
    if x >= 30 and x < 90:    #blue
        pen.color(colors[0])
    elif x >= 90 and x < 150:  #green
        pen.color(colors[1]) 
    elif x >= 150 and x < 210:  #red
        pen.color(colors[2])
    elif x >= 210 and x < 270:  #brown
        pen.color(colors[3]) 
    elif x >= 270 and x < 330: #yellow
        pen.color(colors[4])
    elif x >= 330 and x < 390: #white
        pen.color(colors[5])
    elif x >= 390 and x < 450: #black
        pen.color(colors(6))               
    else:
        pen.color()
        
  else:
       square(x,y)
             
pen.hideturtle()
turtle.onscreenclick(click_check, 1)
turtle.listen()

turtle.done()

