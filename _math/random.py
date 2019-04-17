# -*- coding:utf-8 -*-

import random

# random() 返回[0,1)之间的随机浮点数
for num in range(0, 3):
    result = random.random()
    print(result)

# 返回[m,n]之间的随机整数,注意m <= n
for num in range(0, 3):
    result = random.randint(1, 10)
    print(result)

     
# 返回 i 到 j 之间间隔为 m 的随机整数
for num in range(0, 3):
    result = random.randrange(1, 100, 2)
    print(result)


# 返回m到n之间的随机浮点数
for num in range(0, 3):
    result = random.uniform(1.1, 5.4)
    print(result)


# 返回从序列tab中随机选取一个元素
strTab = ['one', 'two', 'three', 'four', 'five']
for num in range(0, 3):
    result = random.choice(strTab)
    print(result)

# 将序列中的元素顺序打乱
numTab = [1, 3, 5, 6, 7]
newnumTab = random.shuffle(numTab) 
random.shuffle(numTab)
print(newnumTab)            # 无返回，故为None
print(numTab)               # [3, 5, 6, 1, 7]

'''
随机生成有效的11位手机号码

简要说明下：
前三位: 网络识别号，比如移动，联通，电信，号码区段如下：
    电信：133,149,153,173,177,180,181,189,191,199
    联通：130,131,132,145,155,156,166,171,175,176,185,186
    移动：134,135,136,137,138,139,147,150,151,152,157,158,159,172,178,182,183,184,187,188,198
中间四位: 地区编码，每位的范围为[0,9]
最后四位：MDN号码，即用户被叫时，主叫用户所需拨打的号码，每位的范围为[0,9]

摘自：https://baike.baidu.com/item/%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%A0%81/1417348?fr=kg_qa

'''

# 网络识别号列表
identyList = [
    # 电信
    [133,149,153,173,177,180,181,189,191,199],
    # 联通            
    [130,131,132,145,155,156,166,171,175,176,185,186],
    # 移动     
    [134,135,136,137,138,139,147,150,151,152,157,158,159,172,178,182,183,184,187,188,198],
]

# 生成随机号码,count为生成的个数
def createRandPhone(count=10):
    # 获取前三位的随机索引
    randIndex = random.randint(0, len(identyList)-1)
    # 随机号码生成个数
    for _ in range(0, count):
        firstStr = str(random.choice(identyList[randIndex]))
        lastStr = ''
        # 获取后8位随机字符
        for i in range(0, 8):
            lastStr = lastStr + random.choice("0123456789")
        print(u'随机手机号为: ' + firstStr + lastStr)

createRandPhone(5)
