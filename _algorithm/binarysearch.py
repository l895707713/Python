# -*- coding:UTF-8 -*-
#!/usr/bin/env python

'''
二分查找又称折半查找
优点： 比较次数少，查找速度快，平均性能好
缺点：其表数据为有序表，且插入删除困难
适用于不经常变动而查找频繁的有序列表
最优/最坏时间复杂度:O(1) ~ O(logN)
'''

# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def binary_search(_list, searchNum):
    low = 0                             # 最小数下标
    high = len(_list) - 1               # 最大数下标

	# low <= high时才能证明中间有数
    index = 1
    while low <= high:
        mid = (low+high)/2              # 中间数下标 
        print(u'查找的次数为:{0}, low = {1}, high = {2} mid = {3}'.format(index, low, high, mid))
        guess = _list[mid]
        if guess == searchNum:
            return mid
        elif guess > searchNum:         # 中间数大于指定数字，最大数下标移动  
            high = mid - 1
        else:
            low = mid + 1  

        index += 1             
    
    return None 

if __name__ == '__main__':
    maxCount = input(u'请输入列表的最大数值:'.encode('gbk'))
    searchNum = input(u'请输入要查找的数值:'.encode('gbk'))

    print(u'搜寻顺序列表,数据为0 ~ {0}, 查找:{1}'.format(maxCount, searchNum))
    index = binary_search(range(maxCount), searchNum)
    print(u'查找出的索引为:'+ str(index))