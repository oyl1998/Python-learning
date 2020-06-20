
def unit_conversion():
    '''英制单位英寸与公制单位厘米互换'''
    value = float(input('输入长度：'))
    unit = input('输入单位')
    if unit == 'in' or unit == '英寸':
        print('{:.2f}英寸 = {:.2f}厘米'.format(value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('{:.2f}厘米 = {:.2f}英寸'.format(value, value / 2.54))
    else:
        print('请输入有效的单位')

def achievements_transformation():
    '''百分制成绩转换为等级制成绩'''
    score = float(input('输入成绩'))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('对应的等级是:', grade)

def triangle_perimeter_area():
    '''输入三条边长，如果能构成三角形就计算周长和面积'''
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        print('周长: {:.2f}'.format(a + b + c))
        # 海伦公式
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5 # 开根号
        print('面积: {:.2f}'.format(area))
    else:
        print('不能构成三角形')