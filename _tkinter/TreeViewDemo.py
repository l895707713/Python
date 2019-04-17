#!/usr/bin/python
# -*- coding: utf-8 -*-
import ttk          # 用于导入Treeview模块
import random       # 用于导入随机数模块
import Tkinter      # 用于导入GUI Tkinter
from Tkinter import *

# 获取随机数据列表
def getRandomDataList(maxCount=50):
    nameTab = [
        '王硕','李华','张康','李欣','王甜','雨欣','何东','张硕','斯迪','志和','海洋','康路',
        '新鑫','姜帧','赵龙','李天','佳智','江阳','刘菲','季华','雨泽','张华','凶恶','善良',
        '万科','华硕','戴尔','联想','神州','袁田','孔泽','樊支','阿达','东方','南翔','欧尼',
    ]

    dataList = []
    for num in range(0, maxCount):
        data = {}
        # 姓名
        data['name'] = random.choice(nameTab)
        # 排名
        data['rank'] = random.randint(10, 100)
        # 性别
        if num % 2 == 0:
            data['sex'] = 'man'
        else:
            data['sex'] = 'woman'
        # 数学分
        data['Math'] = random.randint(60, 100)
        # 英语分
        data['English'] = random.randint(10, 100)
        dataList.append(data)

    return dataList

# 标题排序: Treeview、列名、排列方式
def sortColumn(tv, col, reverse):
    data = [(tv.set(k, col), k) for k in tv.get_children('')]
    # 排序方式(reverse为False时，表示从小到大)
    data.sort(reverse=reverse)
    # 根据排序后索引移动
    for index, (val, k) in enumerate(data):
        tv.move(k, '', index)
    # 重写标题,使之成为再点倒序的标题
    tv.heading(col, command=lambda: sortColumn(tv, col, not reverse))

class TreeViewDemo():
    # root 父窗口节点
    def __init__(self, root):
        self.root = Tkinter.Toplevel(root)
        self.root.title('TreeView')
        self.createWidgets()

        self.dataTab = []
                
    def createWidgets(self):
        Label(self.root, text="学生信息: ", fg='blue').grid(row=1, column=0)
        # treeView相关
        col = ['1', '2', '3', '4', '5']
        self._treeView = ttk.Treeview(self.root, height=10, show='headings', columns=col)
        # 添加拖曳条相关
        # do something 

        # 设置列相关,不显示
        self._treeView.column('1', width=70, anchor='center')
        self._treeView.column('2', width=60, anchor='center')
        self._treeView.column('3', width=80, anchor='center')
        self._treeView.column('4', width=80, anchor='center')
        self._treeView.column('5', width=80, anchor='center')
        
        # 设置显示表头相关
        self._treeView.heading('1', text='姓名', command=lambda: sortColumn(self._treeView, '1', False))
        self._treeView.heading('2', text='排名', command=lambda: sortColumn(self._treeView, '2', False))
        self._treeView.heading('3', text='性别', command=lambda: sortColumn(self._treeView, '3', False))
        self._treeView.heading('4', text='数学', command=lambda: sortColumn(self._treeView, '4', False))
        self._treeView.heading('5', text='英语', command=lambda: sortColumn(self._treeView, '5', False))

        self._treeView.pack(side='left', fill='both')
        self._treeView.grid(row=2, padx=20)

        # 写入数据
        debugList = getRandomDataList()
        for data in debugList:
            if type(data).__name__ == 'dict':
                 self._treeView.insert('', 'end', values=(data['name'], data['rank'], data['sex'], data['Math'], data['English']))

        # 绑定事件
        self._treeView.bind('<ButtonRelease-1>', self.treeViewEvt1) 

        # 按钮相关
        Button(self.root, text="确认", command=self.ok).grid(row=6, pady=10)

    # 条目点击事件   
    def treeViewEvt1(self, event):
        self.dataTab = []
        for item in self._treeView.selection():
            item_text = self._treeView.item(item, "values")
            self.dataTab.append(item_text)
            print(item_text)
        
    # 确认事件
    def ok(self):
        print('您点击了确认按钮')
        #self.destory()  # 销毁窗口

# 主窗口
class MainWnd():
    def __init__(self):
        self.root = Tkinter.Tk()            # 创建Tkinter对象
        self.root.title('信息概况')          # 标题
        self.initUI()                       # 初始化UI相关
        self.root.mainloop()                # 消息循环

    def initUI(self):
        Label(self.root, text="三好学生", fg='red').grid(row=1, column=0)
        Label(self.root, text="个人信息：").grid(row=2, column=0, sticky='w')
        self.localInput = Text(self.root, width=80, height=5)
        self.localInput.grid(row=3, column=0)

        Button(self.root, text='选择', command=self.selectEvt).grid(row=4, column=0, sticky='e',padx=200)
        Button(self.root, text='确认', command=self.sureEvt).grid(row=4, column=0,sticky='w',padx=200)

    def selectEvt(self):
        TreeViewDemo(self.root)

    def sureEvt(self):
        print(u'您点击了确认事件')

if __name__ == '__main__':
    MainWnd()

