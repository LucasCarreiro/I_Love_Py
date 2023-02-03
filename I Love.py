from tkinter.font import ITALIC
from turtle import *
import turtle

t = turtle.Turtle()

color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
t.write('I Love You', font=('Black Chancery',60,'italic'))
t.color('Red')
turtle.done()