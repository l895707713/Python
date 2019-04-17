#!usr/bin/python
# -*- coding:utf-8 -*-

import os
import re 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 文件模块
class Tool:
    def __init__(self, sourcepath, outpath, strFormat):
        self._sourcepath = sourcepath       # 源文件目录
        self._outpath = outpath             # 输出目录
        self._format = strFormat            # 转换的文件格式
        #
        self.analysisFiles()

    # 获取需要筛选的文件列表
    def getValidFiles(self):
        validpaths = [] 
        # 判定其路径是否是一个存在的文件
        if os.path.isfile(self._sourcepath):
            if self._format != '.all':
                if self._sourcepath.endswith(self._format):
                    validpaths.append(self._sourcepath)
            else:
                validpaths.append(self._sourcepath) 
        # 判定其路径是否是一个存在的目录
        elif os.path.isdir(self._sourcepath):
            for item in os.listdir(self._sourcepath):
                filepath = os.path.join(self._sourcepath, item)
                # 判定文件是否为一个存在的文件
                if os.path.isfile(filepath):
                    if self._format != '.all':
                        if filepath.endswith(self._format):
                            validpaths.append(filepath)
                    else:
                        validpaths.append(filepath) 
        else:
            print('Error: the file is nil, the filePath:' + self._sourcepath)
            return ''

        return validpaths
    
    # 遍历文件列表
    def analysisFiles(self):
        validpaths = self.getValidFiles()
        if validpaths == '':
            print(u'没有遍历的文件，请重新确认')
            return 

        content = ''
        outpath = os.path.join(self._outpath, 'language.txt')
        for filename in validpaths:
            print(u'\n解析的文件为:' + filename)
            content = u'提取的文件名为:\n' + filename + '\n'
            content = content + self.getFileContent(filename) + '\n'
            print(u'' + content)
            # 写入文件
            file_obj = open(outpath, 'a+')
            file_obj.write(content)
            file_obj.close()

        

    # 获取文件内容
    def getFileContent(self, fileName):
        content = ''
        f = open(fileName, 'r')
        line = f.readline()
        while line:
            # 提取每一行的中文字符串
            line = self.extractFile(line.strip())
            if line != '':
                content = content + line + '\n'
            line = f.readline()
        
        f.close()
        return content

    # 提取中文内容
    def extractFile(self, content):
        # 判定字符串是否存在中文
        isExist = self.isContainChinese(content)
        if isExist == False:
            return ''
        #print(u'原内容为：' + content)
        # 获取字符串"的起始位置
        startpos = content.find('"') 
        # 获取字符串"的结束位置              
        endpos = content.find('"', startpos+1) 
        # 截取字符串     
        newStr = content[startpos:endpos+1] 
        #print(u'提取内容为：' + newStr)       
        return newStr

    # 判定字符串是否存在中文
    def isContainChinese(self, content):
        # 转换字符串
        content = content.decode('utf-8', 'ignore')
        # 中文的编码范围是：\u4e00 - \u9fa5
        pattern = re.compile(u'[\u4e00-\u9fa5]')
        match = pattern.search(content)
        if match:
            return True
        return False
