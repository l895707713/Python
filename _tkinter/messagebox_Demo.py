# -*- coding:utf-8 -*-

'''
测试环境: windows7
Python版本： 2.7
'''

import Tkinter
from Tkinter import *
import tkMessageBox as mb           # 导入消息框

# 消息框模块
class MsgBox:
    def __init__(self):
        # 目录相关
        self.root = Tkinter.Tk()
        self.root.title("MessageBox Demo")
        self.root.geometry('300x400')
        self._initUI()
        self.root.mainloop()
    
    # 初始化
    def _initUI(self):
        Button(self.root, text='showinfo', command=self._showInfoWnd).grid(row=1, column=0)
        Button(self.root, text='showwarning', command=self._showWarnWnd).grid(row=2, column=0)
        Button(self.root, text='showerror', command=self._showErrorWnd).grid(row=3, column=0)

        Button(self.root, text='askquestion', command=self._showAskquestion).grid(row=4, column=0)
        Button(self.root, text='askokcancel', command=self._showAskokcancel).grid(row=5, column=0)
        Button(self.root, text='askyesno', command=self._showAskyesno).grid(row=6, column=0)
        Button(self.root, text='askyesnocancel', command=self._showAskyesnocancel).grid(row=7, column=0)
        Button(self.root, text='askretrycancel', command=self._showAskretrycancel).grid(row=8, column=0)

    def _showInfoWnd(self):
       result = mb.showinfo('INFO', '这是个提示框')
       print(result)        # 返回字符串：ok

    def _showWarnWnd(self):
        result = mb.showwarning('WARNING', '这是个警告框')
        print(result)       # 返回字符串：ok

    def _showErrorWnd(self):
        result = mb.showerror('ERROR', '这是个错误框')
        print(result)       # 返回字符串：ok

    def _showAskquestion(self):
        result = mb.askquestion('QUESTION', '这是个显示 是(Y)/否(N) 的提示框')
        print(result)       # 返回字符串：yes/no

    def _showAskokcancel(self):
        result = mb.askokcancel('QUESTION', '这是个显示 确定/取消 的提示框')
        print(result)       # 返回bool：True/False

    def _showAskyesno(self):
        result = mb.askyesno('QUESTION', '这是个显示 是(Y)/否(N) 的提示框') 
        print(result)       # 返回bool：True/False

    def _showAskyesnocancel(self):
        result = mb.askyesnocancel('QUESTION', '这是显示 是(Y)/否(N)/取消 的提示框')
        print(result)       # 返回bool类型：True/False 或者 None

    def _showAskretrycancel(self):
        result = mb.askretrycancel('QUESTION', '这是个显示 重试(R)/取消 的提示框') 
        print(result)       # 返回结果：True/False



if __name__  == "__main__":
    messageBox = MsgBox()

