import turtle
import turtle as t
from random import choice

from jovian.utils.request import retry

# import colorgram as c
#
# colors=c.extract("image.jpg",10)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb=(r,g,b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)


tim=t.Turtle()
tim.speed("fastest")
turtle.colormode(255)
color_list=[(249, 28, 48), (23, 241, 29), (1, 10, 30), (22, 35, 242), (39, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100)]

tim.penup()
tim.hideturtle()
def return_position():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(15*50)
    tim.setheading(0)



tim.setheading(220)
tim.forward(450)
tim.setheading(0)


for _ in range(13):
    for _ in range(15):
        tim.dot(20,choice(color_list))

        tim.forward(50)

    return_position()









screen=t.Screen()
screen.exitonclick()