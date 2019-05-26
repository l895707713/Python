# coding:utf-8

import turtle as t
'''
设置画布(canvas),即绘图区域，主要有两个方法：
'''
t.setup(650, 350, 200, 200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor('blue')
t.seth(-40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)

t.circle(40, 80/2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2/3)
t.done()
