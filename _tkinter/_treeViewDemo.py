# coding:utf-8
#!/usr/bin/env python

import sys
import ttk          	# 用于导入Treeview相关
import Tkinter     		# 用于导入Tkinter相关
from Tkinter import *

'''
文件格式：
    路径：
    后缀名：
    状态：主要有 Add(新增), Delete(删除), Modify(修改), Undefined(未定义) 
    修改人：
    最新修改时间：
'''
debugList = [
    {'path': 'branch_project_game/src/UI/1.py', 'ext': 'lua', 'status': 'Add', 'Author': 'jiangzhen', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/2.py', 'ext': 'csd', 'status': 'Delete', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/3.py', 'ext': 'png', 'status': 'Modify', 'Author': 'liuxinxin', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/4.py', 'ext': 'app', 'status': 'Delete', 'Author': 'zhaoqinglong', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/5.py', 'ext': 'h', 'status': 'Modify',  'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/6.py', 'ext': 'c', 'status': 'Modify', 'Author': 'liuxinxin', 'Time': '1991/11/12'},
    {'path': 'branch_project_game/src/UI/7.py', 'ext': 'hpp', 'status': 'Modify', 'Author': 'wangxuhe', 'Time': '1920/18/12'},
    {'path': 'branch_project_game/src/UI/8.py', 'ext': 'java', 'status': 'Delete', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/9.py', 'ext': 'js', 'status': 'Modify', 'Author': 'zhangshuo', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/11.py', 'ext': 'dyli', 'status': 'Delete', 'Author': 'liuxinxin', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/12.py', 'ext': 'lua', 'status': 'Add', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/13.py', 'ext': 'csd', 'status': 'Delete', 'Author': 'wangxuhe', 'Time': '1190/18/12'},
    {'path': 'branch_project_game/src/UI/14.py', 'ext': 'png', 'status': 'Modify', 'Author': 'zhaoqinglong', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/15.py', 'ext': 'app', 'status': 'Delete', 'Author': 'zhaoqinglong', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/16.py', 'ext': 'h', 'status': 'Modify',  'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/17.py', 'ext': 'c', 'status': 'Modify', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/18.py', 'ext': 'hpp', 'status': 'Modify', 'Author': 'wangxuhe', 'Time': '1290/18/12'},
    {'path': 'branch_project_game/src/UI/19.py', 'ext': 'java', 'status': 'Delete', 'Author': 'liuxinxin', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/20.py', 'ext': 'js', 'status': 'Modify', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/21.py', 'ext': 'dyli', 'status': 'Delete', 'Author': 'wangxuhe', 'Time': '4990/18/12'},
    {'path': 'branch_project_game/src/UI/22.py', 'ext': 'lua', 'status': 'Add', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/23.py', 'ext': 'csd', 'status': 'Delete', 'Author': 'zhaoqinglong', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/24.py', 'ext': 'png', 'status': 'Modify', 'Author': 'liuxinxin', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/25.py', 'ext': 'app', 'status': 'Delete', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/26.py', 'ext': 'h', 'status': 'Modify',  'Author': 'liuxinxin', 'Time': '90/18/12'},
    {'path': 'branch_project_game/src/UI/27.py', 'ext': 'c', 'status': 'Modify', 'Author': 'wangxuhe', 'Time': '10/18/12'},
    {'path': 'branch_project_game/src/UI/28.py', 'ext': 'hpp', 'status': 'Modify', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/29.py', 'ext': 'java', 'status': 'Delete', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/30.py', 'ext': 'js', 'status': 'Modify', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
    {'path': 'branch_project_game/src/UI/31.py', 'ext': 'dyli', 'status': 'Delete', 'Author': 'wangxuhe', 'Time': '1990/18/12'},
]

# 标题排序: Treeview、列名、排列方式
def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    # 排序方式
    l.sort(reverse=reverse)
    # 根据排序后索引移动
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    # 重写标题，使之成为再点倒序的标题
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


class MsgBox():
    def __init__(self):
		self.root = Tkinter.Tk()
		self.root.title('提交确认')
		self.root.geometry('770x320')
		self.initUI()
		self.root.mainloop()
                
    def initUI(self):
        Label(self.root, text="修改文件: ", fg='blue').grid(row=1, column=0, sticky="w")
        # ------------------------------- TreeView ---------------------------
        col = ['1', '2', '3', '4', '5']
        self._treeView = ttk.Treeview(self.root, height=7, show='headings', columns=col)
        # 设置列相关，不显示
        self._treeView.column('1', width=400, anchor='center')
        self._treeView.column('2', width=50, anchor='center')
        self._treeView.column('3', width=60, anchor='center')
        self._treeView.column('4', width=100, anchor='center')
        self._treeView.column('5', width=150, anchor='center')
        # 设置显示表头相关
        self._treeView.heading('1', text='path', command=lambda: treeview_sort_column(self._treeView, '1', False))
        self._treeView.heading('2', text='ext', command=lambda: treeview_sort_column(self._treeView, '2', False))
        self._treeView.heading('3', text='status', command=lambda: treeview_sort_column(self._treeView, '3', False))
        self._treeView.heading('4', text='Author', command=lambda: treeview_sort_column(self._treeView, '4', False))
        self._treeView.heading('5', text='Time', command=lambda: treeview_sort_column(self._treeView, '5', False))

        self._treeView.pack(side='left', fill='both')
        self._treeView.grid(row=2, column=0)

		# 写入数据
        for data in debugList:
            if type(data).__name__ == 'dict':
                 self._treeView.insert('', 'end', values=(data['path'], data['ext'], data['status'], data['Author'], data['Time']))

        # 绑定事件
        self._treeView.bind('<ButtonRelease-1>', self.treeviewClick) 
        # ------------------------------- TreeView ---------------------------

        Label(self.root, text="提交日志: ", fg='red').grid(row=3, column=0, sticky="w")
        self.localInput = Text(self.root, width=110, height=5)
        self.localInput.grid(row=4, column=0)

        Button(self.root, text="确认提交", command=self.ok).grid(row=5, column=0, padx=50)

    # 条目点击事件   
    def treeviewClick(self, event):
        for item in self._treeView.selection():
            item_text = self._treeView.item(item, "values")
            print(item_text)
    
    # 确认提交事件
    def ok(self):
        print(u'您点击了确认提交!!!')



if __name__ == '__main__':
	MsgBox()
