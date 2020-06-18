
def get_suffix(filename, has_dot=False) -> str:
    '''
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    '''
    pos = filename.rfind('.') # rfind(str, begin, end)返回str最后出现的位置，否则返回-1
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

def max2(x):
    '''
    设计一个函数返回传入的列表中最大和第二大的元素的值
    :param x: 整数列表
    :return: 最大和第二大的值
    '''
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2