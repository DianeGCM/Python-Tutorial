import turtle
from typing import DefaultDict
import PIL

planetsdict = {"Mercury": ["", 0,0,0],  "Venus": ["", 0,0,0] }
pen = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(1500, 1200)
wn.bgpic('solarsys.gif')
 

#def default_planet  
#
# 
def check_planet(x, y):
   for j in planetsdict:
      k = planetsdict[j][2]
      print(planetsdict[j][0])
      print(k, "vs" , x)
      if x >= k and x < (k + 5):
          l = planetsdict[j][3]
          print(l, "vs", y)
          if y >= l and y < (l+5):
             q1 = wn.textinput("Quiz Mode", "Which planet is this?")
             if q1 == planetsdict[j][0]:
                wn.textinput("congratulations", "Continue?" )
           

def switch_planet(c, a, x, y):
   planetsdict[c] = [c, a, x, y]
   

def clik_img(x, y):
   pen.up() 
   pen.goto(x, y)
   a = pen.stamp()
   label = wn.textinput("Edit Mode", "Enter the planet name?")
   switch_planet(label, a, x, y)
   print(planetsdict)
   turtle.listen()
   turtle.onkey(equit, "q")
   

def quiz1(x, y):
   pen.up()
   check_planet(x, y)
   

pen.hideturtle()
pen.shape("square")

pen.shapesize(1,1,1)
pen.color("white")

def equit():
  
  usrmode = wn.textinput("Get Mode", "Type I to Input or Q for Quiz")
  if usrmode == "I":
   turtle.listen()
   turtle.onscreenclick(clik_img, 1)
   turtle.onkey(equit, "q")
  else:
   if usrmode == "Q":
    turtle.listen()
    turtle.onscreenclick(quiz1, 1)
    turtle.onkey(equit, "q")

equit()
turtle.done()
