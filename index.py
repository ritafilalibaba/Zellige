from turtle import*
import turtle


bgcolor('#ADA797')
def losange(lenght):
    speed(10)
    pensize(2)
    pencolor('gold')
    left(45)
    forward(lenght)
    for i in range(3):
        left(90)
        forward(lenght)


def motif_final():
   # for j in range(2):
        #penup()
        #goto(x, y)
        #pendown()
        for i in range(8):
            if (i + 1) % 2 ==0:
                color = '#486ED9'
            else:
                color = '#1D2D59'
            fillcolor(color)
            begin_fill()
            losange(45)
            end_fill()

def frise():
    for i in range(6):
        motif_final( )
        penup()
        forward(90)
        pendown()
        turtle.dot(10)
        penup()
        forward(90)
        pendown()
        motif_final()

def pavage():
    l = [-250, -100, 50, 200]
    for i in range(4):
        penup()
        goto(-525,l[i])
        pendown()
        frise()

#frise()
tracer(0,0)
pavage()
hideturtle()


mainloop()
mainloop()
