#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 官网：http://www.pygal.org/en/stable/documentation/types/radar.html

import pygal

# 参数：True为填充
pygal_Radar = pygal.Radar(fill=True)

pygal_Radar.title = 'pygal_Radar'

pygal_Radar.x_labels = ['Attack', 'Defense', 'Charm', 'Health', 'Strike']
pygal_Radar.add('Example1', [60, 80, 98, 20, 85])
pygal_Radar.add('Example2', [30, 50, 78, 70, 65])

pygal_Radar.render_to_file('pygal_Radar.svg')
