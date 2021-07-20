import turtle
from turtle import Turtle as t, Screen as sc
import random

# Create necessary objects
tim = t(shape="turtle")
tim.speed("slow")
screen = sc()
screen.setup(width=500, height=400)
tim.penup()

colors = ["red", "green", "blue", "yellow", "maroon", "orange"]

race_end = False
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Pick up a color from "
                                                          "'red', 'green', 'blue', 'yellow', 'maroon', 'orange': ")

if user_bet not in colors:
    screen.bye()
    print("You've entered a wrong color, the race couldn't happen.")
else:
    turtle_number = []
    for color in colors:
        new_turtle = tim.clone()
        new_turtle.color(color)
        turtle_number.append(new_turtle)

    tim.hideturtle()

    y_cor = -125
    for each_turtle in range(len(turtle_number)):
        turtle_number[each_turtle].goto(-240, y_cor)
        y_cor += 50

    while not race_end:
        for turtle in turtle_number:
            if turtle.xcor() < 230:
                next_position = random.randint(0, 10)
                turtle.forward(next_position)
            else:
                race_end = True
                if turtle.fillcolor() == user_bet:
                    print(f"You've won! The {turtle.fillcolor()} turtle is the winner.")
                else:
                    print(f"You've lost! The {turtle.fillcolor()} turtle is the winner.")

    screen.exitonclick()
