#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 官网：http://www.pygal.org/en/stable/documentation/types/line.html

import pygal

# 创建线形图的类型
#pygal_line = pygal.Line()                             # 简单的线形图
pygal_line = pygal.StackedLine(fill=True)              # 叠加的线形图,参数为空，表示不填充
#pygal_line = pygal.HorizontalLine()                   # 水平线形图
#pygal_line = pygal.HorizontalStackedLine(fill=True)   # 水平叠加的线形图

pygal_line.title = 'pygal_Line'
pygal_line.x_title = 'x_title'
pygal_line.y_title = 'y_title'

pygal_line.x_labels = map(str, range(2002, 2013))
pygal_line.add('Firefox', [None, None, 0,    16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
pygal_line.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
pygal_line.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
pygal_line.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
pygal_line.render_to_file('pygal_Line.svg')
