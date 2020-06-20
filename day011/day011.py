
def main1():
    f = open('a.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()

def main2():
    f = None
    try:
        f = open('a.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()

def main3():
    try:
        # 使用 with as 操作已经打开的文件对象（本身就是上下文管理器），
        # 无论期间是否抛出异常，
        # 都能保证 with as 语句执行完毕后自动关闭已经打开的文件。
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')

import json
def main4():
    '''写JSON文件'''
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
        '''
        json_str = json.dumps(data) 将一个Python数据结构转换为JSON
        data = json.loads(json_str) 将一个JSON转换为Python数据结构
        处理文件时使用如下：
        json.dump(data, f)
        data = json.load(f)
        '''
    except IOError as e:
        print(e)
    print('保存数据完成!')

import requests
def main5():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main5()
