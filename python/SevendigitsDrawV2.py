# SevenDigitsDrawV2.py
import turtle
import time
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            #turtle.fd(60)
            turtle.penup()
            turtle.right(90)
            turtle.fd(50)
            turtle.pendown()
            turtle.write("年",font=("Arial",80,"normal"))
            turtle.pencolor("green")
            turtle.penup()
            turtle.left(180)
            turtle.fd(50)
            turtle.right(90)
            turtle.fd(100)
        elif i == '=':
            #turtle.fd(60)
            turtle.write("月",font=("Arial",50,"normal"))
            turtle.pencolor("blue")
            turtle.fd(60)
        elif i == '+':
            turtle.write("日",font=("Arial",50,"normal"))
            turtle.fd(60)
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(1000,600,200,200)
    turtle.penup()
    turtle.fd(-500)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    #drawDate('8888')
    turtle.hideturtle()
    turtle.done()
main()
    
    
    
