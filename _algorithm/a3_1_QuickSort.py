# -*- coding:UTF-8 -*-
#!/usr/bin/env python

'''
快速排序
简介：采用D&C(divide and conquer)分而治之方法，一种著名的递归式问题解决方法。
思想：
1. 从数列中取出一个数作为基准值
2. 分区，将数列中比基准值大的数放在右边区间，比基准值小的数放在左边区间
3. 重复第1，2步，知道左右各区间仅剩下一个数
时间：O(N * logN)
'''
import sys

def quickSort(arr):
    # 数组为空或者仅有一个元素，无需排序
    if len(arr) < 2:
        return arr 

    # 基准值
    pivot = arr[0]
    # 小于基准值元素组成的数列
    lessArr = [i for i in arr[1:] if i <= pivot]
    # 大于基准值元素组成的数列
    greatArr = [i for i in arr[1:] if i > pivot]

    print(pivot, lessArr, greatArr)
    return quickSort(lessArr) + [pivot] + quickSort(greatArr)

if __name__ == '__main__':
    arr = [-5,10,8,16,0,20,1,4,-10,-7,-8]
    print(u'排序前的数组:{}'.format(arr))
    newArr = quickSort(arr)
    print(u'排序后的数组:{}'.format(newArr))