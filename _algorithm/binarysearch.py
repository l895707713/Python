# coding:utf-8

'''
二分查找又称折半查找
优点： 比较次数少，查找速度快，平均性能好
缺点：其表数据为有序表，且插入删除困难
适用于不经常变动而查找频繁的有序列表
最优/最坏时间复杂度:O(1) ~O(logN)
'''

def binary_search(_list, _num):
    low = 0                             # 最小数下标
    high = len(_list) - 1               # 最大数下标

	# low <= high时才能证明中间有数
    while low <= high:
        mid = (low+high)/2              # 中间数下标 
        print(low, high, mid)
        guess = _list[mid]
        if guess == _num:
            return mid
        elif guess > _num:              # 中间数大于指定数字，最大数下标移动  
            high = mid - 1
        else:
            low = mid + 1               
    
    return None 

if __name__ == '__main__':
    _list = [1,2,3,4,5,6,7,8,9,10]
    index = binary_search(_list, 1)
    print(u'查找出的索引为:'+ str(index))