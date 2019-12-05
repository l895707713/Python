# -*- coding:UTF-8 -*-
#!/usr/bin/env python

'''
线性查找
简介: 按照一定的顺序检查数组中的每个元素，知道寻找到为止。数据越多越耗费时间
时间: O(n)
'''
import sys

# 查找指定值
def line_search(arr, value):
    for i in range(1,len(arr)):
        print(u'-->查找数组中数值:{0}'.format(arr[i]))
        if arr[i] == value:
            return i 
    
    return -1

if __name__ == '__main__':
    arr = [-5,10,8,6,0,5]
    searchValue = 5
    print(u'查找数组:{0}, 查找数值:{1}'.format(arr, searchValue))
    index = line_search(arr,searchValue)
    if index != -1:
        print(u'元素在数组中的索引为{0}'.format(index))
    else:
        print(u'未找到!!!')