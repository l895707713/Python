# -*- coding:utf-8 -*-

'''
测试环境: windows7
Python版本： 2.7
个人博客：https://www.cnblogs.com/SkyflyBird/p/10344019.html
'''
import traceback
import Tkinter
from Tkinter import *
import tkFileDialog

DEF_PATH = 'C:\Python27'        # 设置默认路径

# 消息框模块
class MsgBox:
    def __init__(self):
        # 目录相关
        self.root = Tkinter.Tk()
        self.root.title("tkFileDialog")
        self.showMsgBox()
        self.root.mainloop()
    
    # 显示消息框
    def showMsgBox(self):
        root = self.root           
 
        # 源文件输入框
        Label(root, text='源文件:').grid(row=1, column=0, sticky='E')
        self.csdVar = StringVar()
        self.csdVar.set(DEF_PATH)
        Entry(root, textvariable=self.csdVar, width=50).grid(row=1, column=1)
        Button(root, text='打开文件', command=self.openFileEvent).grid(row=1, column=2)
        Button(root, text='打开目录', command=self.openDirEvent).grid(row=1, column=3)
        
        # 输出框
        Label(root, text='输出:').grid(row=2, column=0, sticky='E')
        self.outVar = StringVar()
        self.outVar.set(DEF_PATH)
        Entry(root,textvariable=self.outVar, width=50).grid(row=2, column=1)
        Button(root, text='另存为', command=self.selectOutPathEvent).grid(row=2, column=2)

    # 
    def openFileEvent(self):
        '''
        @method: askopenfilename
        @function: 选择文件后，会返回显示文件的完整路径，取消的话，会返回空字符
        @params:
            defaultextension: 默认文件的扩展名
            filetypes: 设置文件类型下拉菜单里的的选项
            initialdir: 对话框中默认的路径
            initialfile: 对话框中初始化显示的文件名
            parent: 父对话框(由哪个窗口弹出就在哪个上端)
            title: 弹出对话框的标题
        '''
        newDir = tkFileDialog.askopenfilename(initialdir=DEF_PATH,initialfile='README',title='打开新文件')
        if len(newDir) == 0:
            return
        self.csdVar.set(newDir)
    # 
    def openDirEvent(self):
        '''
        @method: askdirectory
        @function: 打开目录,倘若选择了了文件夹则返回路径，否则返回空字符
        @params: 
            title： 弹出对话框的标题
            initialdir:  对话框中默认的路径
        '''
        newDir = tkFileDialog.askdirectory(initialdir=DEF_PATH,title='打开目录')
        if len(newDir) == 0:
            return
        self.csdVar.set(newDir)

    # 另存为
    def selectOutPathEvent(self):
        '''
        @method: asksaveasfilename
        @function: 另存为
        @param: 其参数与askopenfilename一样，不再赘述
        '''
        newDir = tkFileDialog.asksaveasfilename(initialdir=DEF_PATH)
        if len(newDir) == 0:
            return
        self.outVar.set(newDir)

if __name__  == "__main__":
    try: 
        messageBox = MsgBox()
    except Exception:
        traceback.print_exc()

