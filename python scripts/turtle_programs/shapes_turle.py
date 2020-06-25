import turtle

#Setting up custom window
wn = turtle.Screen()
wn.bgcolor("Pink")

#turtle for making a star
starie = turtle.Turtle()
for x in range(5):
    starie.forward(150)
    starie.right(144)

#turtle for making a triangle
traingie = turtle.Turtle()
traingie.left(180)
traingie.penup()
traingie.forward(100)
traingie.pendown()
traingie.pencolor('brown')
for i in range(3):
    traingie.forward(90)
    traingie.left(120)
  
#tutle for making a square outside in
outsie = turtle.Turtle()
outsie.pencolor('Red')
outsie.left(90)
outsie.penup()
outsie.forward(100)
outsie.left(90)
outsie.forward(100)
outsie.pendown()

def sqr_func(size):
    for m in range(4):
        outsie.forward(size)
        outsie.right(90)
        size = size - 5

sqr_func(160)
sqr_func(140)
sqr_func(120)
sqr_func(100)
sqr_func(80)
sqr_func(60)
sqr_func(40)
sqr_func(20)

#turtle for making a square inside out
insie = turtle.Turtle()
insie.pencolor('blue')
insie.left(90)
insie.penup()
insie.forward(170)
insie.right(90)
insie.forward(100)
insie.pendown()

def sqrin_func(size):
    for n in range(4):
        insie.forward(size)
        insie.left(90)
        size = size + 5

sqrin_func(20)
sqrin_func(40)
sqrin_func(60)
sqrin_func(80)
sqrin_func(100)
sqrin_func(120)
sqrin_func(140)
sqrin_func(160)

wn.exitonclick()

