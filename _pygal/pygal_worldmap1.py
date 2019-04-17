#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
pygal 绘制世界地图
安装方式： pip/pip3 install pygal_maps_world
官网：https://pypi.org/project/pygal_maps_world/
参考网址：https://www.cnblogs.com/keqipu/p/7283991.html
'''

import pygal.maps.world 

# 绘制洲地图
supra = pygal.maps.world.SupranationalWorld()
supra.add('Asia', [('asia', 1)])
supra.add('Europe', [('europe', 1)])
supra.add('Africa', [('africa', 1)])
supra.add('North america', [('north_america', 1)])
supra.add('South america', [('south_america', 1)])
supra.add('Oceania', [('oceania', 1)])
supra.add('Antartica', [('antartica', 1)])
supra.render_to_file('py_worldmap1.svg')

