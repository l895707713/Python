# -*- coding:utf-8 -*-
'''
通用字符编码检测
官网： https://pypi.org/project/chardet/
安装方式：pip/pip3 install chardet
版本要求：pythhon 2.6, 2.7 or 3.3+

'''
import os
import sys 
import codecs
import chardet

# 检测文件
def _detectfile(filename):
    f = open(filename, 'rb')
    byte_str = f.read()

    _dict = chardet.detect(byte_str)
    _dict['path'] = filename
    f.close()

    return _dict 

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(u'请输入您要查找的目录!!!')
        sys.exit()
    
    path = sys.argv[1]
    if os.path.isdir(path) is False:
        print(u'目录不存在!!!')
        sys.exit()
    
    print(u'您查找的目录为:' + path)
    print(u'文件编码格式如下：')
    for root, dirs, files in os.walk(path):
        for filename in files:
            fullpath = os.path.join(root, filename)
            if os.path.isfile(fullpath):
                _dict = _detectfile(fullpath)
                print(_dict)