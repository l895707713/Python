# _*_ coding:utf8 _*_
import os
import datetime

# 返回绝对路径
print(os.path.abspath('path.py')) 						# G:\code\Demo\path.py
print(os.path.abspath('../Demo\\path.py')) 				# G:\code\Demo\path.py
print(os.path.abspath('G:\code\Demo\path.py'))			# G:\code\Demo\path.py

# 是否为绝对路径,若是True，否则False
print(os.path.isabs('path.py')) 						# False
print(os.path.isabs('G:\code\Demo\path.py'))			# True

# 将路径分割为目录和文件名
print(os.path.split('G:\code\Demo\path.py')) 			# ('G:\\code\\Demo', 'path.py')

# 返回文件目录
print(os.path.dirname('G:\code\Demo\path.py')) 			# G:\code\Demo

# 判定是否是一个存在的目录，若是True，否则False
print(os.path.isdir('path.py')) 						# False
print(os.path.isdir('HH:\code')) 						# False
print(os.path.isdir('C:\\windows')) 					# True

# 返回文件名
print(os.path.basename('../Demo\\path.py'))				# path.py
print(os.path.basename('G:\code\Demo\path.py')) 		# path.py

# 分离文件名和后缀
print(os.path.splitext('path.py')) 						# ('path', '.py')
print(os.path.splitext('G:\code\Demo\path.py')) 		# ('G:\\code\\Demo\\path', '.py')

# 判定是否是一个存在的文件,若是True,否则False
print(os.path.isfile('Fuck.text')) 						# False
print(os.path.isfile('path.py')) 						# True
print(os.path.isfile('G:\code\Demo\path.py')) 			# True


# 返回多个路径中，所有path共有的路径(注意:路径一定要存在，否则会返回空)
pathTab = ['G:\code\LuaProject', 'G:\code\Demo', 'G:\code\csdDemo'] 	
print(os.path.commonprefix(pathTab)) 					# G:\code\

print('------------------------------------------------------')
# 将目录和文件名组合在一起
print(os.path.join('G:\Code\Demo', 'path.py')) 			# G:\Code\Demo\path.py
print(os.path.join('G:\code\pathCode','.lua')) 			# G:\code\pathCode\.lua
## 在第一个绝对路径前的参数忽略掉
print(os.path.join('windos','E:\code', 'demo.lua')) 	# E:\code\demo.lua

# 转换路径的大小写和斜杠
print(os.path.normcase('D:/windows\\system32')) 		# d:\windows\system32

# 返回文件的创建时间(浮点型秒数)
timestamp = os.path.getctime('path.py') 				
timestruct = datetime.datetime.fromtimestamp(timestamp)
print(timestruct.strftime('%Y-%m-%d %H:%M:%S'),timestamp) 	# ('2019-01-31 15:13:34', 1548918814.2969258)

# 返回文件最近的访问时间(浮点型秒数)
timestamp = os.path.getatime('path.py') 				
timestruct = datetime.datetime.fromtimestamp(timestamp)
print(timestruct.strftime('%Y-%m-%d %H:%M:%S'),timestamp) 	# ('2019-01-31 15:19:57', 1548919197.053918)

# 返回文件最近修改时间(浮点型秒数)
timestamp = os.path.getmtime('path.py') 				
timestruct = datetime.datetime.fromtimestamp(timestamp)
print(timestruct.strftime('%Y-%m-%d %H:%M:%S'),timestamp) 	# ('2019-01-31 16:33:43', 1548923623.2079258)

# 返回文件的大小(字节)，如果文件不存在就返回错误
print(os.path.getsize('path.py')) 							# 3061
print(os.path.getsize('G:\code\Demo\path.py'))				# 3061
#print(os.path.getsize('file.lua')) 						# WindowsError: [Error 2] : 'file.lua'

# 判定路径是否为链接
print(os.path.islink('G:\code\Demo'))
print(os.path.islink('http://www.baidu.com'))
