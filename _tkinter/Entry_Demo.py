# -*- coding:utf-8 -*-
# __author__ = 'Code~'

import Tkinter                  # 引用Tkinter库
from Tkinter import *           # 导入Tkinter库方法

DEF_PATH = 'C:\Python27'
# 消息框模块
class MsgBox:
    def __init__(self):
        
        # 创建Tkinter对象
        self.root = Tkinter.Tk()
        # 标题
        self.root.title('Tkinter Demo')
        # 设定窗口大小
        self.root.geometry('500x400')
        # 初始化UI相关
        self.initUI()
        # 消息循环
        self.root.mainloop()
    
    # 初始化控件
    def initUI(self):
        #Entry
        # 不可使用text属性来设定
        en0 = Entry(self.root, text='请输入文本...',width=50, bg='red')
        en0.grid(row=1, column=0, sticky='E')
        # 使用StringVar()来绑定Entry，通过set来设定初始化值，通过get来获取，其输入值可改变
        self.inputVar = StringVar()
        self.inputVar.set('请输入内容....')
        en1 = Entry(self.root, textvariable=self.inputVar, width=50,bg='yellow')
        en1.grid(row=2, column=0, sticky='E')
        Button(self.root, text='确认1', command=self.sureEvent1).grid(row=2, column=1)
        # 密码输入框
        self.inputVar2 = StringVar()
        self.inputVar2.set('请输入密码')
        en2 = Entry(self.root, textvariable=self.inputVar2, width=50,show='*')
        en2.grid(row=3, column=0, sticky='E')
        Button(self.root, text='确认2', command=self.sureEvent2).grid(row=3, column=1)
        # 设置输入框属性
        # 属性值有4个：normal(可写),disabled(不可操作), readonly(只读，不可操作),通过state来设定
        self.inputVar3 = StringVar()
        self.inputVar3.set('readonly')
        en3 = Entry(self.root, textvariable=self.inputVar3, width=50,state='readonly')
        en3.grid(row=4, column=0, sticky='E')
        Button(self.root, text='确认3', command=self.sureEvent3).grid(row=4, column=1)
        
    def sureEvent1(self):
        inputStr = self.inputVar.get()
        print(u'您的第二个输入框内容：' + inputStr)

    def sureEvent2(self):
        inputStr = self.inputVar2.get()
        print(u'您的第三个输入框内容：' + inputStr)

    def sureEvent3(self):
        inputStr = self.inputVar3.get()
        print(u'您的第四个输入框内容：' + inputStr)

if __name__  == "__main__":
    messageBox = MsgBox()

