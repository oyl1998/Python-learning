#import this
import turtle

#help(turtle)

def draw_rectangle(x, y, width, height):
    '''绘制矩形'''
    turtle.goto(x, y)
    turtle.pencolor('red')
    # 颜色填充
    turtle.fillcolor('red')
    # 准备开始填充图形
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_star(x, y, radius):
    '''绘制五角星'''
    turtle.setpos(x, y) # 移动到绝对位置
    pos1 = turtle.pos() # 返回(海龟)箭头当前位置坐标
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    # color(pencolor, fillcolor)
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()

def main():
    '''主程序'''
    turtle.speed(12)
    turtle.penup()
    x, y = 0, 0
    # 画国旗主体
    width, height = 540, 360 # 国旗比例是3:2
    draw_rectangle(x, y, width, height)
    # 画大星星
    pice = 20
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    # 隐藏海龟
    turtle.ht()
    turtle.mainloop() # 显示绘图窗口

if __name__ == '__main__':
    main()