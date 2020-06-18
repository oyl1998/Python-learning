'''
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
'''

import random

def generate_code(code_len: int) -> str:
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for i in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    n = int(input('输入验证码的长度'))
    print(generate_code(n))

