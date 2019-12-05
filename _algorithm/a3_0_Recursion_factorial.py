# -*- coding:UTF-8 -*-
#!/usr/bin/env python

'''
-- 递归阶乘
'''
import sys
import math 

'''
设置递归深度，否则在递归阶乘1000时，会报错：
    python maximum recursion depth exceeded(超过python递归深度)
'''
#sys.setrecursionlimit(2000)

# 递归阶乘
def Recursion_factorial(num):
    if num > 1:
        return num * Recursion_factorial(num - 1)

    return 1

# python数学库
def Math_factorial(num):
    return math.factorial(num)

if __name__ == '__main__':
    selectIndex = input(u'请选择计算的方式(1-递归 2-数学库):'.encode('gbk'))
    num = input(u'请输入数字:'.encode('gbk'))
    if selectIndex == 1:
        result = Recursion_factorial(num)
        print(result)
    elif selectIndex == 2:
        result = Math_factorial(num)
        print(result)

