import turtle
turtle.penup()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-180)
turtle.forward(250)
turtle.pendown()
turtle.seth(-40)
for i in range(2):
    #turtle.seth(-40)
    turtle.circle(90,80)
    turtle.circle(-90,80)
    #turtle.circle(80,80)
turtle.seth(0)
turtle.forward(20)
turtle.circle(50)
turtle.seth(-50)
turtle.forward(40)
