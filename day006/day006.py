from math import sqrt

# test1
def gcd(x: int, y: int) -> int:
    '''求最大公约数'''
    (x, y) = (y, x) if x > y else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i

def lcm(x: int, y: int) -> int:
    '''求最小公倍数'''
    return x * y // gcd(x, y)

# test2
def is_palindrome(num: int) -> bool:
    '''判断一个数是不是回文数'''
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp %10
        temp //= 10
    return total == num

# test3
def is_prime(num: int) -> bool:
    '''判断一个数是不是素数'''
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True




