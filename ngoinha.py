import turtle 
turtle.speed(8)
turtle.pensize(5)

turtle.pencolor("blue")
turtle.bgcolor("olive")
turtle.penup()
turtle.goto(-800,-200)
turtle.pendown()
turtle.color("aquamarine")
turtle.begin_fill()
#sky 
for i in range(2):
    turtle.forward(1600)
    turtle.left(90)
    turtle.forward(800)
    turtle.left(90)
turtle.end_fill()
# house
#than 
turtle.penup()
turtle.goto(-600,-200)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
for i in range(2):
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
turtle.end_fill()
#mai
turtle.pencolor("black")
turtle.pencolor("red")
turtle.penup()
turtle.goto(-750,70)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()


turtle.forward(800)
turtle.left(125)
turtle.fd(200)
turtle.left(55)
turtle.fd(510)
turtle.lt(55)
turtle.forward(200)
turtle.left(125)

turtle.end_fill()
#door
turtle.pensize(5)
turtle.pencolor("black")
turtle.penup()
turtle.goto(-370,-200)
turtle.pendown()
turtle.color("gray")
turtle.begin_fill()
for i in range(2):
    turtle.fd(130)
    turtle.lt(90)
    turtle.fd(200)
    turtle.lt(90)
turtle.end_fill()

#windows
turtle.pensize(5)
turtle.pencolor("black")
turtle.penup()
turtle.goto(-550,-40)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
for i in range(4):
    turtle.fd(100)
    turtle.lt(90)
turtle.end_fill()




turtle.end_fill()
turtle.mainloop()