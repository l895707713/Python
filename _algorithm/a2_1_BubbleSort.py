# -*- coding:UTF-8 -*-
#!/usr/bin/env python

'''
冒泡排序
简介：重复遍历要排序的数列，一次比较两个元素，如果数值顺序错误就交换过来，直至到不需要再交换，
时间：O(n*n)
'''
import sys

def bubbleSort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    arr = [-5,10,8,6,0,5]
    print(u'排序前的数组:{}'.format(arr))
    bubbleSort(arr)
    print(u'排序后的数组:{}'.format(arr))