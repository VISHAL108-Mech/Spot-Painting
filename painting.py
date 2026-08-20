import random
import turtle
from turtle import Turtle, Screen

import colorgram

rgb_colors = []
colors = colorgram.extract("img.jpg", 80)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 234),
              (222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40),
              (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83),
              (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44),
              (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181),
              (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72),
              (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121),
              (218, 176, 188), (220, 183, 166), (166, 207, 165),
              (179, 188, 211), (149, 37, 35), (46, 73, 71), (45, 65, 62)]

turtle.colormode(255)
myt = Turtle()
myt.speed(0)
myt.hideturtle()
screen = Screen()
myt.setheading(225)
myt.penup()
myt.forward(400)
myt.setheading(0)

def draw_dot():
    for i in range(10):
        myt.dot(20, random.choice(color_list))
        myt.penup()
        myt.forward(50)

def turn_left():
    myt.setheading(90)
    myt.penup()
    myt.forward(50)
    myt.setheading(180)
    myt.penup()
    myt.forward(50)

def turn_right():
    myt.setheading(90)
    myt.penup()
    myt.forward(50)
    myt.setheading(0)
    myt.penup()
    myt.forward(50)

def one_cycle():
    turn_left()
    draw_dot()
    turn_right()
    draw_dot()

draw_dot()

for i in range(4):
    one_cycle()

turn_left()
draw_dot()

screen.exitonclick()