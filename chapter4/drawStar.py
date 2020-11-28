#draw a star shape

import turtle
wn=turtle.Screen()
biff = turtle.Turtle()

biff.forward(-50)   #starting point
for i in range(5):  #a star has 5 sides
    biff.forward(100)   
    biff.left(216)  #angle for each star turn