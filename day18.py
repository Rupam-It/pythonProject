# challange to draw a squre
import turtle as t
import time 
import random

screen=t.Screen()

# t.forward(100)
# t.right(90) # 1st line 
# t.forward(100)
# t.right(90)    # 2nd line
# t.forward(100)
# t.right(90)   # 3rd line
# t.forward(100)
# t.right(90)  #4th line
# time.sleep(4)



#Q2) draw a dashed line
# for i in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


# #Q3) draw a triangel
# t.setposition(0,0)
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.right(120)
# t.forward(100)


#drawing different shapes with turtle



# this is to draw a triangle
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.setposition(100,0)
# t.right(120)



# #this is to draw a squre
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.setposition(100,0)
# t.right(90)

# # this is a pentagon
# t.right(72)
# t.forward(100)
# t.right(72)
# t.forward(100)
# t.right(72)
# t.forward(100)
# t.right(72)
# t.forward(100)


# this is a generalize code for

# color_list=['black','yellow','green','pink','blue','red','brown']

# t.setposition(0,0)
# t.pencolor(color_list[0])
# t.forward(100) 
# for i in range(3,10):
#     angel=360/i
#     t.setposition(100,0)
#     for j in range(i-1):
#         t.pencolor(color_list[i-3])
#         t.right(angel)
#         t.forward(100)
    
#     t.right(angel)








# #challange 4(A random work)
# directions=[0,90,180,270]
color_list=['black','yellow','green','pink','blue','red','brown']


# t.pensize(15)
# t.speed(10)


# for _ in range(200):
#     t.color(random.choice(color_list))
#     t.forward(30)
#     t.setheading(random.choice(directions))




# q5) draw a spiral
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    color=(r,g,b)
    return color

t.speed(0)
screen.colormode(255) 



# t.color(random_color())
def draw_spiralgraph(size_of_gap):
    for _ in range(360//size_of_gap):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)


draw_spiralgraph(5)

time.sleep(4)
# screen.exitonclick()