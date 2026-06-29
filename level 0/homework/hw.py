from turtle import *


#we want to paint a house

#step 1: draw a square
speed(30)

width(7)
color("purple")
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing the right window

color("brown")
penup()
setheading(0)
goto(140,150)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)


#drawing the left window
penup()
setheading(0)
goto(10,150)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

exitonclick()