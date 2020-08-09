import turtle

screen = turtle.Screen()
screen.bgcolor("lightyellow")

shape = turtle.Turtle("circle")
shape.color("red")

shape.left(180)
size = 20
for i in range(10000) :
 shape.forward(5)
 if abs(shape.xcor()) >= screen.window_width()/2 :
    shape.left(90)
    shape.forward(size)
    size+=10
    shape.left(90)

screen.exitonclick() 
