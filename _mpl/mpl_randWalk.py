#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# matplotlib官网：https://matplotlib.org/

import matplotlib.pyplot as plt
from random import choice 

# 生成随机数据
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 随机值起始点
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while(len(self.x_values) < self.num_points):
            # 设置前进的方向以及这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # 判定是否原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一点的位置
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


if __name__ == '__main__':
    # 注意： 如果绘制的点数很多，程序的运行速度会很慢
    rw = RandomWalk()
    rw.fill_walk()

    # 绘制随机点
    point_nums = list(range(rw.num_points))
    # 突出起点和终点
    plt.scatter(0,0, c='green', edgecolors='none', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20)
    # 使用颜色绘制剩下的点
    plt.scatter(rw.x_values, rw.y_values, c=point_nums, cmap=plt.cm.Blues, edgecolor='none', s=5)
    plt.show()


