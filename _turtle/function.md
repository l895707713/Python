# 使用方式
'''
import turtle 
'''

# 画布即绘图区域相关
'''
方式一：screensize
参数为：宽，高，颜色
'''
#turtle.screensize(canvwidth=400, canvheight=300, bg='blue')

'''
方式二： setup
width, height 为整数时，表示像素；若为浮点数时，表示栈屏幕的比例，默认情况下width为0.5，height为0.75
startx,starty 表示左上角顶点的位置，以像素为单位，默认窗口居中
    若starx为正，表示从左侧开始计算，若为负，则从右侧边缘开始计算
    若starty为正，表示从顶部计算，若为负，表示从下边缘计算
'''
turtle.setup(width=0.5, height=0.75, startx=0, starty=0)

# 画笔相关
# 设置画笔宽度；别名： width
turtle.pensize(width=10)
# 设置画笔的颜色,可使用字符串如"blue"或者RGB值比如(255,2,55)
turtle.pencolor
# 画笔移动时，不绘制；别名： pu | up
turtle.penup()
# 画笔移动时，绘制；别名： pd | down
turtle.pendown()
# 画笔是否在绘制,若pendown则True,若penup则False
turtle.isdown()
# 画笔的绘制速度，取值范围[0,10],其取值范围阶段为：(1,3,6,10,0)分别对应(最慢，慢，正常，快，超快)
turtle.speed(1)

# 移动相关(画笔的起始位置，默认为(0,0))
# 向当前画笔方向移动distance像素长度，别名：fd
turtle.forward(distance=100)
# 向当前画笔反方向移动distance像素长度,别名：back | bk
#turtle.backward(distance=200)
# 顺时针旋转角度,别名：rt
turtle.right(90)
turtle.backward(distance=200)
# 逆时针旋转角度，别名：lt
turtle.left(90)
turtle.backward(distance=100)
# 画笔移动到指定位置，别名:setpos | setposition | goto
turtle.goto(x=0, y=0)
# 绘制圆.参数依次为半径，角度,绘制的步数
# 若半径为正，则圆心在画笔的左边，若为负则在画笔的右边；后两个参数可省略，默认为360度，步数为1
turtle.circle(radius=-100, extent=180, steps=6)
