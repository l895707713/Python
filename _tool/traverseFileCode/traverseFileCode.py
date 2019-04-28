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
    f.close()

    return _dict

# 遍历文件(路径，忽略编码)
def analysisfile(path, ignorelist):
    _map = []
    filenum = 0
    ignorenum = 0
    for root, dirs, files in os.walk(path):
        for filename in files:
            fullpath = os.path.join(root, filename)
            if os.path.isfile(fullpath):
                _dict = _traversefile(fullpath)
                if _dict['encoding'] in ignorelist:
                    ignorenum += 1
                else:
                    print(_dict)
                    _map.append(_dict)
                    filenum += 1
            else:
                print(fullpath + ' is not exsit file!!!')

    print(u'遍历文件数目为:'+ str(filenum))
    print(u'忽略文件格式文件数目为:'+ str(ignorenum))

    # 写入文件
    f = open('output.txt', 'a')
    for item in _map:
        f.write(str(item) + '\n')
    f.close()

if __name__ == '__main__':
    # mac终端命令，不可运行，提示：ImportError: No module named chardet
    print(u'请输入你要分析的目录：')
    path = raw_input()
    print(u'请输入你要忽略的文件编码格式(utf-8,ascii等):')
    ignore = raw_input()

    analysisfile(path,str.lower(ignore))