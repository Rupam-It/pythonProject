# this project is for generate  random clolor in a aqure
import turtle as t
import random

screen=t.Screen()
screen.colormode(255)


screen.bgcolor('white')


# this is the actual color list
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

t.hideturtle()
t.penup()
t.speed(0)
t.setpos(-150,-150)
for j in range(10):
    t.setpos(-150,-150+j*30)
    for i in range(10):
        t.setpos(-150+i*30,-150+j*30)
        t.dot(15,random.choice(color_list))

screen.exitonclick()