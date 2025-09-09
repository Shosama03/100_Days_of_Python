from turtle import Turtle,Screen
from random import choice

turtle_colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "violet",
    "magenta", "cyan", "turquoise", "black", "white", "gray", "grey", "brown",
    "beige", "tan", "gold", "maroon", "navy", "skyblue", "lightgreen",
    "darkgreen", "chocolate", "light salmon","IndianRed"
]
tim=Turtle()
side=3
for _ in range(7):
    tim.color(choice(turtle_colors))
    for _ in range(side):
        tim.forward(100)
        tim.right(360/side)
    side+=1















screen=Screen()
screen.exitonclick()