#draw a clock using turtles
#important methods: stamp, position, shape
import turtle
wn=turtle.Screen()
wn.bgcolor("green")
biff = turtle.Turtle()
biff.shape("turtle")
biff.fillcolor("blue")
biff.color("blue")
biff.penup()
biff.stamp()

for i in range(0, 360, 30):
    biff.left(i)
    biff.forward(50)
    biff.stamp()
    biff.position()
    biff.right(i)
    