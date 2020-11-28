import turtle
wn=turtle.Screen()
biff = turtle.Turtle()

def drawPolygon(num_side, length, color, fill_color):
    angle = 360/num_side
    biff.color(color)
    biff.fillcolor(fill_color)
    biff.speed(1000)
    for i in range(num_side):
        pow(i)
        biff.left(angle)
        biff.forward(length)
    wn.exitonclick()



