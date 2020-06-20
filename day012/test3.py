'''
替换字符串中的不良内容
'''

import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    # sub(pattern, repl, string, count=0, flags=0)
    # 用指定的字符串替换原字符串中与正则表达式匹配的模式
    # 可以用count指定替换的次数
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE) #re.IGNORECASE 忽略大小写匹配标记
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()