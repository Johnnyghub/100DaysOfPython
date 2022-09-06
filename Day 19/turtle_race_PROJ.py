import turtle
import random

race_is_on = True

screen = turtle.Screen()
screen.setup(width=500, height=400)
#screen.bgpic('racetrack.png')  if a background is wanted for the race, however, must change y-coord spacing

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_coord = -100

for i in range(6):
    t = turtle.Turtle()
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    turtles.append(t)
    turtles[i].goto(x=-230, y=y_coord)
    y_coord += 40

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

if bet:
    while race_is_on:
        for turtle in turtles:
            if race_is_on:  # this statement prevents 2 winners from occuring
                if turtle.xcor() > 230:
                    race_is_on = False
                    winning_color = turtle.pencolor()

                    if winning_color == bet:
                        print(f"Congrats! The turtle you bet on has won!")
                    else:
                        print(f"You lost the bet! The {winning_color} turtle has won.")

                turtle.forward(random.randint(0, 10))


screen.exitonclick()
