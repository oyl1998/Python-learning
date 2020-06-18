from math import pi as PI

def temperature_change():
    '''华氏温度转换为摄氏温度。'''
    f = float(input('输入华氏温度：'))
    c = (f - 32) / 1.8
    print('{:.2f}华氏度 = {:.2f}摄氏度'.format(f, c))
    # format 的使用
    # https://www.runoob.com/python/att-string-format.html

def circle_perimeter_area():
    '''输入圆的半径计算计算周长和面积'''
    radis = float(input('输入圆的半径：'))
    perimeter = 2 * radis * PI
    area = PI * radis * radis
    print('周长: {:.2f}'.format(perimeter))
    print('面积: {:.2f}'.format(area))

def judge_leap_year():
    '''输入年份判断是不是闰年'''
    year = int(input('输入年份：'))
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    print(is_leap)

