import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

race_is_on = False
user_bet = screen.textinput("Title Race Game", "Which turtle do you bet on? Choose a color.")
colors = ["red", "orange", "black", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle won.")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle won.")
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)


screen.exitonclick()



