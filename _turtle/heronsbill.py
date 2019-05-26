# coding:utf-8

'''
    太阳花
'''
import turtle as t
t.speed(1)
t.color("red", "yellow")
t.speed(10)
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)
t.end_fill()
t.done()