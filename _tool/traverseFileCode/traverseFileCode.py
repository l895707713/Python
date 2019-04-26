# -*- coding:utf-8 -*-
'''
通用字符编码检测
官网： https://pypi.org/project/chardet/
安装方式：pip/pip3 install chardet
版本要求：pythhon 2.6, 2.7 or 3.3+

'''
import os
import sys 
import chardet

# 分析文件
def _traversefile(filename):
    f = open(filename, 'rb')
    byte_str = f.read()
    '''
    chardet.detect的返回结果:
    encoding: 字符编码
    cofidence: (0.0~1.0) 概率
    languge: 语言
    filepath: (新加) 
    '''
    _dict = chardet.detect(byte_str)
    _dict['filepath'] = filename
    print(_dict)
    f.close()

    return _dict

# 遍历文件
def analysisfile(path):
    _map = []
    filenum = 0
    for root, dirs, files in os.walk(path):
        for filename in files:
            fullpath = os.path.join(root, filename)
            if os.path.isfile(fullpath):
                _dict = _traversefile(fullpath)
                _map.append(_dict)
                filenum += 1
            else:
                print(fullpath + ' is not exsit file!!!')

    print('遍历文件数目为:'+ str(filenum))

    # 写入文件
    f = open('output.txt', 'a+')
    for item in _map:
        f.write(str(item) + '\n')
    f.close()

if __name__ == '__main__':
    # 终端命令，不可运行，提示：ImportError: No module named chardet
    '''
    if len(sys.argv) != 1:
        print('Error: please input source path!!!')
        sys.exit()
    
    path = sys.argv[1]
    print(path)
    '''
    path = 'src'
    analysisfile(path)