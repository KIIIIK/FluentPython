import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
"""
namedtuple的用法
就是给元组加上一个名字,增加可读性
"""
Point = collections.namedtuple('Ponit', ['x', 'y'])
p = Point(11, y=22)
p[0] + p[1]
x, y = p
x, y
p.x + p.y
p
#可以用现有的序列或者可迭代对象去实例化一个namedtuple




class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + [list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

















