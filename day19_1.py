# this is a project of tuttle race
import turtle as t
import random as r



is_race_on=False


screen=t.Screen()
screen.colormode(255)
screen.setup(width=500, height=400)

user_bet=screen.textinput(title="Make your bet ",prompt='which turtle will win the race ? enter a color')
colors=['red','orange','yellow','green','blue','purple']
all_turtles=[]


for i in range(6):
    new_turtle=t.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y=-150+i*55)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color== user_bet:
                print(f"you've own! the {winning_color} turtle win the race..")
            else:
                print(f"you are lost! the {winning_color} turtle win the race..")


        rand_distance=r.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()