'''
奥特曼打小怪兽
'''

from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    '''战斗者'''

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        '''
        初始化方法
        :param name: 名字
        :param hp: 生命值
        '''
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property #@property装饰器就是负责把一个方法变成属性调用的
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        '''
        攻击
        :param other: 被攻击对象
        :return:
        '''
        pass

class Ultraman(Fighter):
    '''奥特曼'''

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        '''
        初始化方法
        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        '''
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        '''
        终极必杀技
        :param other: 被攻击对象
        :return: 使用成功True否则False
        '''
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        '''
        魔法攻击
        :param other: 被攻击群体
        :return: 使用成功True否则False
        '''
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        '''恢复魔法值'''
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return f'~~~{self._name}奥特曼~~~\n' + \
            f'生命值:{self._hp}\n' + \
            f'魔法值:{self._hp}\n'

class Monster(Fighter):
    '''小怪兽'''

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return f'~~~{self._name}小怪兽~~~' + f'生命值:{self._hp}'

def is_any_alive(monsters):
    '''判断有没有小怪兽活着'''
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    '''
    选择一个活着的小怪兽
    :param monsters: 怪兽集
    :return: 一个怪兽
    '''
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def dispaly_info(ultraman, monsters):
    '''显示奥特曼和小怪兽的信息'''
    print(ultraman)
    for monster in monsters:
        print(monster, end='')

def main():
    u = Ultraman('迪迦', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第{:0>2d}回合========'.format(fight_round))
        m = select_alive_one(ms)
        skill = randint(1, 10) # 随机选择技能
        if skill <= 6: # 60%的概率使用普通攻击
            print(f'{u.name}使用了普通攻击，打了{m.name}.')
            u.attack(m)
            print(f'{u.name}的魔法值恢复了{u.resume()}点.')
        elif skill <= 9: # 30%的概率使用魔法攻击
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻击.')
            else:
                print(f'{u.name}使用魔法攻击失败.')
        else: # 10%的概率使用终极必杀技
            if u.huge_attack(m):
                print(f'{u.name}使用了终极必杀技虐了{m.name}')
            else:
                print(f'{u.name}使用普通攻击打了{m.name}.')
                print(f'{u.name}的魔法值恢复了{u.resume()}点.')
        if m.alive > 0: # 如果选中的小怪兽没有死就回击奥特曼
            print(f'{m.name}回击了{u.name}')
            m.attack(u)
        dispaly_info(u, ms)
        fight_round += 1
        print('\n========战斗结束!========\n')
        if u.alive > 0:
            print(f'{u.name}奥特曼胜利!')
        else:
            print('小怪兽胜利!')

if __name__ == '__main__':
    main()


