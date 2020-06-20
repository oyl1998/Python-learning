from random import randint
from math import sqrt

def find_daffodil_number():
    ''''找出所有水仙花数'''
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)

def money_chicken():
    '''百钱百鸡问题'''
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: {}只, 母鸡: {}只, 小鸡: {}只'.format(x, y, z))

def Craps():
    '''CRAPS赌博游戏'''
    money = 100
    while money > 0:
        print('你的总资产为：', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注'))
            if 0 < debt <= 100:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了{}点'.format(first))
        if first == 7 or first == 11:
            print('玩家胜')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了{}点'.format(current))
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了，游戏结束！')

#prictice

def Fibonacci():
    '''生成斐波那契数列的前20个数'''
    f = [1, 1]
    for i in range(2, 20):
        x = f[-1] + f[-2]
        f.append(x)
    print(f)

def perfect_number():
    '''找出10000以内的完美数'''
    for num in range(1, 10000):
        result = 0
        for factor in range(1, int(sqrt(num)) + 1):
            if num % factor == 0:
                result += factor
                if factor > 1 and num // factor != factor:
                    result += num // factor
        if result == num:
            print(num)

def get_prime_number():
    '''输出100以内所有的素数'''
    for i in range(2, 100):
        is_prime = True
        for x in range(2, int(sqrt(i)) + 1):
            if i % x == 0:
                is_prime = False
                break
        if is_prime:
            print(i)


