def vexoanoc():
    a = 20
    import turtle
    t= turtle.Turtle()
    t.speed(100)
    t.pencolor("black")
    un =0
    while un<100:
        t.circle(a+un,45)
        un+=1
    t.done()
if __name__=="__main__":
    vexoanoc()