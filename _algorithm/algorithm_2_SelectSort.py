# -*- coding:UTF-8 -*-
#!/usr/bin/env python

'''
选择排序
原理： 从未排序的序列中找到最小(大)元素，存放到新序列中，然后再从未排序的剩余的序列中继续查找，直到末尾。
'''
import sys

# 查找最小原色
def FindSmallest(arr):
    smallest = arr[0]           # 默认最小值
    smallIndex = 0              # 默认最小值索引

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallIndex = i 
    
    return smallIndex

# 选择排序
def SelectSort(arr):
    newArr = []
    for i in range(len(arr)):
        print(u'--> 查找序列:{0}'.format(arr))
        # 查找数组中最小元素索引
        smallIndex = FindSmallest(arr)
        # 原有数组移除指定值
        smallValue = arr.pop(smallIndex)
        # 将值放置到新列表中
        newArr.append(smallValue)

    return newArr


if __name__ == '__main__':
    arr = [-5,10,8,6,0,5]
    print(u'未排序序列:{0}'.format(arr))
    newArr = SelectSort(arr)
    print(u'已排序序列:{0}'.format(newArr))