import turtle
import math
import random

# setting up a screen
window = turtle.Screen()
window.bgcolor('black')

#Turle features
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
rotate = int(360)
# drawing the mandala
def drawMandala(turtie, size):
    for i in range(10):
        turtie.circle(size)
        size = size-4

def drawSpecial(turtie, size, repeat):
    for i in range(repeat):
        drawMandala(turtie,size)
        turtie.right(360/repeat)
drawSpecial(Albert,100,10)

Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate = int(90)
# drawing the mandala
def drawMandala(turtie, size):
    for i in range(4):
        turtie.circle(size)
        size = size-10

def drawSpecial(turtie, size, repeat):
    for i in range(repeat):
        drawMandala(turtie,size)
        turtie.right(360/repeat)
drawSpecial(Steve,100,10)

Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
rotate = int(80)
# drawing the mandala
def drawMandala(turtie, size):
    for i in range(4):
        turtie.circle(size)
        size = size-5

def drawSpecial(turtie, size, repeat):
    for i in range(repeat):
        drawMandala(turtie,size)
        turtie.right(360/repeat)
drawSpecial(Barry,100,10)

Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
rotate = int(90)
# drawing the mandala
def drawMandala(turtie, size):
    for i in range(4):
        turtie.circle(size)
        size = size-19

def drawSpecial(turtie, size, repeat):
    for i in range(repeat):
        drawMandala(turtie,size)
        turtie.right(360/repeat)
drawSpecial(Terry,100,10)

Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate = int(90)
# drawing the mandala
def drawMandala(turtie, size):
    for i in range(4):
        turtie.circle(size)
        size = size-20

def drawSpecial(turtie, size, repeat):
    for i in range(repeat):
        drawMandala(turtie,size)
        turtie.right(360/repeat)
drawSpecial(Will,100,10)

turtle.getscreen()._root.mainloop()