#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import os
import sys
import xlrd
import fnmatch

# 添加设置默认编码，避免python2.7运行报错：UnicodeEncodeError: 'ascii' codec can't encode characters ...
reload(sys)
sys.setdefaultencoding('utf-8')

'''
excel 表数据格式：
# 前三行分别为： 中文名称，英文, 数据类型
商品ID	商品名称	道具数量	商品价格	商品当前库存	总库存	有否邮箱发送	开始刷新时间
itemId	itemName  int	  int	  int	     int	  isEmail	updateTime
number	string	 number	 number	  number	number	   bool	      date

# 若数字为空，则默认为'nil'
1007	食用油1升	1	5000	10	1000	1	2018-11-09 00:00:00
1008	烧烤架	1	7000	10	1000	1	2018-11-09 00:00:00
1009	煮蛋器	1	5000	10	1000	1	2018-11-09 00:00:00
1010	护眼小台灯	1	5000	10	1000	0	2018-11-09 00:00:00
1011	50元充值卡	1	5000	10	1000	1	2018-11-09 00:00:00
'''

# 源文件目录路径
SRC_PATH = 'src'
# 输出文件目录路径
OUT_PATH = 'out'
# 表头数据
'''
headdict = {
    # 主要用于注释
    [1] = ['商品ID', '商品介绍', '商品价格', ...],
    # 如果参数存在"_"，比如：_itemState表示此处列数据忽略
    [2] = ['itemId', 'itemState', 'price', ...], 
    # 主要用于判定数据的类型，类型主要有如下几种：
        bool: 布尔类型，若为0，转换为false, 若为 > 1 的数值，转换为true
        number: 数字，包含整型，浮点型等
        string: 字符串
        data: 表数据，推荐格式:{100,1,30} 或者 {{1,2,3}, {3,4,5}}
        date: 日期,类似于2010-08-09 12:00 
    [3] = ['number','string','number', ...],
}
'''


# 获取表头数据相关，即前三行的中文名，英文名，类型
def getHeadDict(sheet):
    headdict = {}
    cols = sheet.ncols
    for row in range(0, 3):
        _list = []
        for col in range(0, cols):
            cell = sheet.cell(row, col)         # 获取单元格对象
            celltype = cell.ctype               # 获取单元格数据类型
            cellvalue = cell.value              # 获取单元格数值
            '''
            cell.ctype的几种属性：
                0：empty
                1：string
                2：number
                3：date
                4：boolean
                5：error
            '''
            if(celltype != 1):
                print('[excel] sheet found invalid col name, col:' + str(col))
            else:
                # 将对象值存储到列表中
                _list.append(str(cellvalue))
        # 将列表存储到字典中
        headdict[row] = _list
    return headdict


# 解析每行数据
def getRowList(rowIndex, sheet, headdict):
    row_list = []
    cols = sheet.ncols
    for col in range(0, cols):
        cell = sheet.cell(rowIndex, col)
        ctype = cell.ctype
        
        # 判定是否存在"_"，若存在，则忽略掉此列数据
        k = headdict[1][col]
        if str(k).startswith('_'):
            continue

        # 根据类型整合数据
        head_type = headdict[2][col]
        if head_type == 'bool':
            # 布尔类型
            if ctype == 0:
                v = 'false'
            elif ctype == 2:
                if v > 0:
                    v = 'true'
                else:
                    v = 'false'
        elif head_type == 'number':
            # 数字
            if ctype == 0:
                v = 'nil'
            else:
                v = cell.value
        elif head_type == 'string':
            # 字符串
            if ctype == 0:
                v = '\"\"'
            else:
                v = '\"%s\"' % (cell.value)
        elif head_type == 'data':
            # 表数据
            if ctype == 0:
                v = '{}'
            else:
                v = cell.value
        elif head_type == 'date':
            # 日期
            v = cell.value
        else:
            v = cell.value

        # 加入列表
        row_list.append([k, v])
    return row_list


# 转换
def excel2lua(root, filename):
    filepath = os.path.join(root, filename)
    # 打开excel文件读取数据
    workbook = xlrd.open_workbook(filepath, encoding_override='utf-8')
    # 获取所有工作表的名字
    sheetNames = workbook.sheet_names()
    # 遍历sheets表
    for index in range(len(sheetNames)):
        # 通过索引顺序获取指定工作表数据
        sheet = workbook.sheet_by_index(index)
        rows = sheet.nrows  # 获取指定工作表的有效行数
        cols = sheet.ncols  # 获取指定工作表中的有效列数
        print('[excel] sheetname:{0} (row:{1}, col:{2})'.format(sheet.name, rows, cols))

        # 获取头文件数据
        headdict = getHeadDict(sheet)
        # 构造行数据
        excel_dict = {}
        for row in range(3, rows):
            # 获取ID对象
            cellId = sheet.cell(row, 0)
            ctype = cellId.ctype  # 类型
            value = cellId.value  # 数值
            if(ctype != 2):
                print('[excel] row:{} id is not number'.format(row))
                continue
            # 获取指定行数据，并将数据存储到列表中
            excel_dict[value] = getRowList(row, sheet, headdict)

        # 写入文件，输出文件名格式为: excelname_sheetname.lua
        outname = os.path.splitext(filename)[0] + '_' + sheetNames[index] + '.lua'
        outpath = os.path.join(OUT_PATH, outname)
        newfile = open(outpath, 'w')
        newfile.write('local config = {\n')
        for k, v in excel_dict.items():
            newfile.write('\t[' + str(int(k)) + '] = {\n')
            for row_data in v:
                newfile.write('\t\t{0} = {1},\n'.format(row_data[0], row_data[1]))
            newfile.write('\t},\n')

        newfile.write('}\n return config\n')
        newfile.close()
        print('write filepath:{} sucess'.format(outpath))


# 遍历src文件下目录
def walkFiles():
    for root, dirs, files in os.walk(SRC_PATH):
        for filename in fnmatch.filter(files, "*.xlsx"):
            excel2lua(root, filename)


if __name__ == '__main__':
    walkFiles()