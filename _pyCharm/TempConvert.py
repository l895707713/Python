#!/usr/bin/env python3
# coding:utf-8

'''
* 变量命名首字符不可为数字，且不可为关键字，主要有：
    and, elif, import, raise, global, as, else, in, return, nonlocal, del
    assert, except, is, try, True, break, finally, lambda, while, False,
    class, for, not, with, Node, continue, from, or, yield, def, if, pass
* 缩进是python程序的格式框架，缩进不正确会导致程序运行错误
* eval: 去掉字符串参数最外层的引号，比如"
    eval('1+2')  -> 3
    eval("'1+2'") -> 1+2
    eval('print("pyCharm")') -> pyCharm#!/usr/local/bin
'''

# 温度转换
inputStr = input('请输入带有符号的温度值：')
if inputStr[-1] in ['F', 'f']:
    # 华氏温度
    C = (eval(inputStr[0:-1]) - 32)/1.8
    print('转换后的温度是{:.2f}C'.format(C))
elif inputStr[-1] in ['C', 'c']:
    # 摄氏温度
    F = 1.8 * eval(inputStr[0:-1]) + 32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print('输入格式有误!!!')
