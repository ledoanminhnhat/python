#khai báo 
from random import random
import turtle
import time
import random

dừng = 0.1

# điểm
điểm =0 
điểm_cao=0

#tạo màn hình
sk= turtle.Screen()
sk.title("Game Rắn")
sk.bgcolor('blue')
sk.setup(width=600,height=600)
sk.tracer(0)

#tao con trỏ đầu rắn 
đầu = turtle.Turtle()
đầu.speed(0)
đầu.shape("square")
đầu.color("black")
đầu.penup()
đầu.goto(0,0)
đầu.direction ="stop"

# Mồi rắn
thuc_an=turtle.Turtle()
thuc_an.speed(0)
thuc_an.shape("square")
thuc_an.color("red")
thuc_an.penup()
thuc_an.goto(0,100)

nhieu_phan=[]

#Bản điểm
bd= turtle.Turtle()
bd.speed(0)
bd.shape("square")
bd.color("black")
bd.penup()
bd.hideturtle()
bd.goto(0,260)
bd.write("điểm: 0  điểm cao nhất: 0", align= "trung tâm", font=("ds-digital", 24,"normal"))

#chuc nang
def di_len():
    if đầu.direction !="down":
        đầu.direction="up"
def di_xuong():
    if đầu.direction !="up":
        đầu.direction= "down"
def re_trai():
    if đầu.direction !="right":
        đầu.direction= "left"
def re_phai():
    if đầu.direction !="left":
        đầu.direction= "right"
def move():
    if đầu.direction =="up":
        y = đầu.ycor()
        đầu.sety(y+20)
    if đầu.direction =="down":
        y = đầu.ycor()
        đầu.sety(y-20)
    if đầu.direction =="left":
        x= đầu.xcor()
        đầu.xcor(x-20)
    if đầu.direction =="right":
        x= đầu.xcor()
        đầu.xcor(x+20)

#thiết lập nút điều khiển
sk.listen()
sk.onkeypress(di_len,"w")
sk.onkeypress(di_xuong,"s")
sk.onkeypress(re_phai,"d")
sk.onkeypress(re_trai,"a")

while True:
    sk.update()
    #kiem tra 
    if đầu.xcor()>290 or đầu.xcor()<-290 or đầu.ycor()>290 or đầu.ycor()<-290:
        time.sleep(1)
        đầu.goto(0,0)
        đầu.direction = "stop"
        #ẩn đoạn cơ thể
        for đoạn in nhieu_phan:
            đoạn.goto(1000,1000) #giới hạn
        #xóa tất cả đoạn cơ thể
        đoạn.clear()
        #làm mới điểm
        điểm=0
        #làm mới dừng
        dừng =0.1

        bd.clear()
        bd.write("điểm:{} điểm cao nhất:{}".format(điểm, điểm_cao),align= "trung tâm",font=("ds-digital",24,"normal"))
    #kiểm tra va chạm với mồi
    if đầu.distance(thuc_an)<20:
        #di chuyển thức ăn đến nơi bất kì
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        thuc_an.goto(x,y)

        # thêm một đoạn thân cho rắn
        đoạn_mới= turtle.Turtle()
        đoạn_mới.speed(0)
        đoạn_mới.shape("square")
        đoạn_mới.color("black")
        đoạn_mới.penup()
        nhieu_phan.append(đoạn_mới)

        #giảm thời gian chờ
        dừng -= 0.001
        #tăng điểm 
        điểm += 10

        if điểm >điểm_cao:
            điểm_cao= điểm
        bd.clear()
        bd.write("điểm:{} điểm cao nhất:{}".format(điểm, điểm_cao),align= 'trung tâm',font=("ds-digital",24,"normal"))
    #di chuyển các đoạn đến nơi định trc
    for index in range(len(nhieu_phan)-1,0,-1):
        x = nhieu_phan[index-1].xcor()
        y = nhieu_phan[index-1].ycor()
        nhieu_phan[index].goto(x,y)
    # di chuyển đoạn 0 đến đầu
    if len(nhieu_phan)>0:
        x= đầu.xcor()
        y= đầu.ycor()
        nhieu_phan[0].goto(x,y)
    move()

    # kiểm tra từng đoạn với cơ thể
    for đoạn in nhieu_phan:
        if đoạn.distance(đầu)<20:
            time.sleep(1)
            đầu.goto(0,0)
            đầu.direction ="stop"
            #ẩn đoạn
            for đoạn in nhieu_phan:
                đoạn.goto(1000,1000)
            nhieu_phan.clear()
            điểm=0
            dừng=0.1

            #cập nhật điểm
            bd.clear()
            bd.write("điểm:{} điểm cao nhất:{}".format(điểm, điểm_cao),align= 'trung tâm',font=("ds-digital",24,"normal"))
    time.sleep(dừng)

    sk.mainloop()


        