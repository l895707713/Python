#### 简介
将excel文件转化为lua配置文件，需要python xlrd的支持，安装方式为：
```
pip/pip3 install xlrd
```
#### 说明
将要转换的excel文件放置到src目录中
excel文件可有多个，且每个excel文件中可有多个sheet
输出文件在out目录中，且文件名为:excelname_sheetname.lua
```
使用命令：
python excellua.py
```
