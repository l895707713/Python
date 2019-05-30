#!/usr/bin/python
# coding:utf-8

import time
import turtle 

colors = ['red', 'yellow', 'purple', 'blue']

turtle.speed(10)
turtle.pensize(2)
turtle.bgcolor('black')
for index in range(0, 400):
    turtle.forward(2 * index)
    turtle.pencolor(colors[index % 4])
    turtle.left(90)             # 角度可进行修改，查看效果

turtle.done()