#### 简介
将excel文件转化为lua配置文件，需要python xlrd库的支持，安装方式为：
```
pip/pip3 install xlrd
```
#### 使用方法
将要转换的excel文件放置到src目录中，excel文件可有多个且excel文件中也可包含多个sheet表

然后在cmd或者终端下输入命令：
```
python excellua.py
```
#### 注意事项
1. excel文件需要关闭的情况下，才可执行，否则报错
2. excel文件命名，禁止使用中文命名，且sheet命名禁止使用中文，否则会有乱码

#### 命名规则
1. 如果excel有多个sheet的话，其命名格式为：ExcelName_SheetName + Config.lua
2. 如果excel只有一个sheet的话，其命名格式为： ExcelName + Config.lua


#### excel编写要求
第一行：中文简介,比如：成就ID， 描述， 任务类型等，在生成的配置文件中做为注释使用

第二行：变量名称

第三行：数据类型，有如下几种：
```    
int: 整型数字，若空着，程序默认为 nil，填写的数字形式如下： 99
float: 浮点型数字，若空着，程序默认为nil，填写的数字形式如下： 2.15
bool: 布尔类型，若空着，默认为false；也可填写数字，若 > 0 程序为true, 若 <= 0 程序为false
string: 字符串，若空着，程序默认为""
data: 表数据，若空着，默认为{}，填写方式待定
date: 日期，待定
```
第四行，相关的列表数据

|成就ID	|描述	|任务类型	|完成条件	|是否邮箱发送|	奖励类型|	奖励数目| 
| --------   | -----:   | :----: | -----:   | :----: | -----:   | :----: |
|itemId	|itemName	|tasktype	|count	|isEmail	|rewardtype	|rewardnum|
|int	|string	|int	|int	|bool	|int	|float|
| 1001 |	玩家升到2级|	1|	2|	1| 5|	10.9|

#### lua脚本样式
```
--[[
	itemId: [number] 成就ID
	itemName: [string] 描述
	tasktype: [number] 任务类型（1 等级 2 金币 3 章节 4 击杀敌人数目）
	isEmail: [bool] 是否邮箱发送
	rewardtype: [number] 奖励类型(1金币 2体力 3弹药 4钻石 5勋章)
	rewardnum: [number] 奖励数目
]]

local AchieveConfig = {
	[1024] = {itemId = 1024,itemName = "",tasktype = 4,count = 40000,isEmail = true,rewardtype = 5,rewardnum = 33,},
  ...
}
return AchieveConfig
```

#### xlrd参考
[python xlrd读取excel](https://www.cnblogs.com/SkyflyBird/p/10944107.html "标题")