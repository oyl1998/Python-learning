'''
从一段文字中提取出国内手机号码
'''

import re

def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    # compile(pattern, flags=0) 编译正则表达式返回正则表达式对象
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    # pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # findall(pattern, string, flags=0)	查找字符串所有与正则表达式匹配的模式 返回字符串的列表
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    # finditer(pattern, string, flags=0)	查找字符串所有与正则表达式匹配的模式 返回一个迭代器
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    # search(pattern, string, flags=0)
    # 搜索字符串中第一次出现正则表达式的模式
    # 成功返回匹配对象 否则返回None
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()