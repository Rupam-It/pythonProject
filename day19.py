import turtle as t


screen=t.Screen()
# #vedio no 177 


# def move_forward():
#     t.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forward)


#vedio no 178(make the turtle to move back word and forward)
def move_forward():
    t.forward(10)

def move_backword():
    t.backward(10)


def move_left():
    t.left(10)

def move_right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()



screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backword)
screen.onkey(key='a',fun=move_left)
screen.onkey(key='d',fun=move_right)
screen.onkey(key='c',fun=clear)



screen.exitonclick()


