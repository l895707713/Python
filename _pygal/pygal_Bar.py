#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 官网：http://www.pygal.org/en/stable/documentation/types/bar.html

import pygal

# 创建条形图的类型
#bar = pygal.Bar()                  # 简单的条形图
#bar = pygal.StackedBar()           # 叠加的条形图
#bar = pygal.HorizontalBar()        # 水平条形图
bar = pygal.HorizontalStackedBar()  # 水平叠加的图形图

bar.title = 'pygal_Bar'
bar.x_title = 'x_title'
bar.y_title = 'y_title'

bar.x_labels = map(str, range(1,7))
bar.add('Example1', [155, 167, 168, 170, 159, 181])
bar.add('Example2', [55, 67, 68, 70, 59, 81])
bar.add('Example3', [105, 17, 178, 100, 179, 81])
bar.render_to_file('pygal_Bar.svg')
