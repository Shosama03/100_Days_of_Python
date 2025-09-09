import random
import turtle
from turtle import Turtle, Screen
from random import choice

from streamlit import radio

tim=Turtle()


turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    new_color=(r,g,b)
    return new_color



tim.pensize(5)
tim.speed("fastest")
directions=[0,90,180,270]
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))



screen=Screen()
screen.exitonclick()