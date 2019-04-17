#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# matplotlib官网：https://matplotlib.org/

import matplotlib.pyplot as plt

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]      # 计算平方值

# 设置标题
plt.title('Square Demo', fontsize=24)
# 设置坐标轴标签
plt.xlabel('X+', fontsize=14)
plt.ylabel('Y+', fontsize=14)

# 设置刻度标记的大小
#plt.tick_params(axis='both', labelsize=14)

# 设置每个坐标轴的取值范围
# 前两个参数为x的取值范围，后两个参数为y的取值范围
plt.axis([0,100, 0,10000])

# 绘制点(x位置，y位置，点的颜色,线条宽度)
plt.scatter(x_values, y_values, c='red', s=1)

# 绘制图形，并设定线条的粗细
#plt.plot(x_values, y_values - 100, linewidth=1)

# 打开matplotlib查看器，并显示绘制图形
plt.show()

'''
若将程序图标保存到文件中，可将show替换为savafig
第一个参数表示保存的文件名
第二个参数表示是否将图标多余的空白区域剪切掉
plt.savefig('mpl_squares.png',bbox_inches='tight')
'''
