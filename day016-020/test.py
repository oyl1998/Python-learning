'''
常用算法等
https://github.com/oyl1998/Python-100-Days/blob/master/Day16-20/16-20.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md
'''


def Comprehensions():
    '''生成式的推导'''
    price = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    price2 = {key:value for key, value in price.items() if value > 100}
    print(price2)

def nested_lists():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 录入五个学生三门课程的成绩
    # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # scores = [[None] * len(courses)] * len(names)
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for  col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}的成绩：'))
    print(scores)

import heapq
def hash_sort():
    '''
    从列表中找出最大的或最小的N个元素
    堆结构(大根堆/小根堆)
    :return: NULL
    '''
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    # 前3个最大的
    print(heapq.nlargest(3, list1))
    # 前3个最小的
    print(heapq.nsmallest(3, list1))

    # 排序规则用 key自定
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

import itertools
def itertools_module():
    ''' 迭代工具模块'''

    # 产生ABCD的全排列
    it = itertools.permutations('ABCD')
    # 产生ABCDE的五选三组合
    it = itertools.combinations('ABCDE', 3)
    # 产生ABCD和123的笛卡尔积
    it = itertools.product('ABCD', '123')
    for i in it:
        print(i)
    # 产生ABC的无限循环序列
    it = itertools.cycle(('A', 'B', 'C'))

from collections import Counter
def collections_module():
    '''
    collections模块
    常用的工具类：
    namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
    deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素是，deque会表现出更好的性能，渐近时间复杂度为O(1)。
    Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。
    OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
    defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。
    '''

    # 找出序列中出现次数最多的元素
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(3))

def select_sort(items, comp=lambda x, y: x < y):
    '''
    简单选择排序
    :param items: 待排序列表
    :param comp: 比较函数，默认为升序
    :return: 排序后的列表
    '''
    items = items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(items, comp=lambda x, y: x < y):
    '''
    冒泡排序
    :param items: 待排序列表
    :param comp: 比较函数，默认是升序
    :return: 排序后的列表
    '''
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - i - 1):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1],  items[j]
                swapped = True
        if not swapped:
            break
    return items

def merge(items1, items2, comp=lambda x, y: x < y):
    '''
    合并(将两个有序的列表合并成一个有序的列表)
    :param items1: 列表1
    :param items2: 列表2
    :param comp: 比较函数，默认为升序
    :return: 合并后的列表
    '''
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def _merge_sort(items, comp):
    return merge(list(items), comp)

def merge_sort(items, comp=lambda x, y: x < y):
    '''
    归并排序
    :param items: 待排序列表
    :param comp: 比较函数，默认为升序
    :return: 排序后的列表
    '''
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)

def seq_search(items, key):
    '''
    顺序查找
    :param items: 列表
    :param key: 查找元素
    :return: 所在位置，否则为-1
    '''
    for index, item in enumerate(items):
        if items == key:
            return index
    return -1

def bin_search(items, key):
    '''
    折半查找
    :param items: 列表
    :param key: 查找元素
    :return: 所在位置，否则为-1
    '''
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

