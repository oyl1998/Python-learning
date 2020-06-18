'''
计算指定的年月日是这一年的第几天
'''

def is_leap_year(year):
    '''
    判断年份是否是闰年
    :param year: 年份
    :return: 闰年返回True否则返回False
    '''
    return year % 4 == 1 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    '''
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 是该年的第几天
    '''
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))

if __name__ == '__main__':
    main()
