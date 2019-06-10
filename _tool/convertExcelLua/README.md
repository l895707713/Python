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
(注意：不可在打开excel文件的情况下，运行否则会报错)
```

#### excel格式设定
```
# 前三行分别为： 中文名称，英文, 数据类型
商品ID	商品名称	道具数量	商品价格	商品当前库存	总库存	有否邮箱发送	开始刷新时间    # 第一行主要用于做注释
itemId	itemName  int	  int	  int	     int	  isEmail	updateTime                   # 第二行主要用于作为key，若添加"_"表示该列废弃，不再读取
n umber	string	 number	 number	  number	number	   bool	      date               # 第三行主要用于作为检索value的判定

# 若数字为空，则默认为'nil'或者-1
# 针对于bool，倘若拓展，可能为True或者true,因此可以编写为数字形式，若 <=0 表示false， 若 > 0 表示true
# 针对于日期，针对情况判定是否转换为描述，或者其他，脚本暂时没有添加处理
1007	食用油1升	1	5000	10	1000	1	2018-11-09 00:00:00
1008	烧烤架	1	7000	10	1000	1	2018-11-09 00:00:00
1009	煮蛋器	1	5000	10	1000	1	2018-11-09 00:00:00
1010	护眼小台灯	1	5000	10	1000	0	2018-11-09 00:00:00
1011	50元充值卡	1	5000	10	1000	1	2018-11-09 00:00:00
```

#### 导出文件格式设定
```
假设excel名为mall, 表中存在Item，Gold， Diamond等，命名格式为:
  excelname_sheetname_config.lua
建议文件命名以英文命名，避免因中文而导致的读取失败的问题
```
