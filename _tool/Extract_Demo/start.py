#!usr/bin/python
# -*- coding:utf-8 -*-

import os
import Tkinter
import tkFileDialog
from Tkinter import *
from fileTool import Tool

# 默认文件目录
SOURCE_FILE = 'sourceFile'
DEST_FILE = 'outFile'

# 转换的文件格式
FORMATE = ['.lua', '.py', '.all']


# 消息框模块
class MsgWnd:
    def __init__(self):
        # 目录相关
        self.sourcepath = os.path.abspath(SOURCE_FILE)
        self.outpath = os.path.abspath(DEST_FILE)

        self.root = Tkinter.Tk()
        self.root.title('提取中文工具')
        self.showMsgBox()
        self.root.mainloop()
    
    # 显示消息框
    def showMsgBox(self):
        #
        Label(self.root, text='源文件目录:').grid(row=1, column=0, sticky='E')
        Button(self.root, text='...', command=self.selSourcePathEvt).grid(row=1, column=2, sticky='E', padx='10')
        self.csdVar = StringVar()
        self.csdVar.set(self.sourcepath)
        Entry(self.root, textvariable=self.csdVar, width=50).grid(row=1, column=1)
        
        #
        Label(self.root, text='输出目录:').grid(row=2, column=0, sticky='E')
        Button(self.root, text='...', command=self.selOutPathEvt).grid(row=2, column=2, sticky='E', padx='10')
        self.outVar = StringVar()
        self.outVar.set(self.outpath)
        Entry(self.root,textvariable=self.outVar, width=50).grid(row=2, column=1)
        #
        Label(self.root, text='转换格式:').grid(row=3, column=0, sticky='E')
        self.radioVar = IntVar()
        for i in range(len(FORMATE)):
            Radiobutton(self.root, text=FORMATE[i], variable=self.radioVar, value=i).grid(row=3, column=1, sticky='W', padx=60*i)
        #
        Button(self.root, text='确认', command=self.sureEvent).grid(row=4, column=1)

    # 选择源文件目录事件
    def selSourcePathEvt(self):
        newDir = tkFileDialog.askdirectory(initialdir=self.sourcepath)
        if len(newDir) == 0:
            return

        self.csdVar.set(newDir)
        self.sourcepath = newDir

    # 选择输出目录事件
    def selOutPathEvt(self):
        newDir = tkFileDialog.askdirectory(initialdir=self.outpath)
        if len(newDir) == 0:
            return

        self.outVar.set(newDir)
        self.outpath = newDir

    def sureEvent(self):
        formatIndex = self.radioVar.get()
        strFormat = FORMATE[formatIndex]
        # 判定目录是否合法
        if len(self.sourcepath) == 0:
            print(u'请设置源文件目录')
            return 
        elif len(self.outpath) == 0:
            print(u'请设置输出目录')
            return 
        elif os.path.exists(self.sourcepath) is False:
            print(u'源文件目录不存在，请重新设置')
        elif os.path.exists(self.outpath) is False:
            print(u'存储目录不存在，请重新设置')

        print(u'打开的文件目录为:' + self.sourcepath)
        print(u'另存为的文件目录为:' + self.outpath)
        print(u'提取的格式为:' + strFormat)
        Tool(self.sourcepath, self.outpath, strFormat)

if __name__  == "__main__":
    msgbox = MsgWnd()

