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
t = [11, 12]
Point._make(t)
#可以将namedtuple对象转化成有序字典OrderedDict
##有序字典和通常字典类似，只是它可以记录元素插入其中的顺序，而一般字典是会以任意的顺序迭代的。
p = Point(x=11, y=22)
p_ = p._asdict()
p_['x']
p_['y']
for x, y in p_.items():
    print(x, y)
#通过这个方法我们可以实现对指定name的元素的值进行替换
p = Point(x=11, y=22)
p._replace(x=33)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
len(deck)
#由__getitem__方法提供
deck[0]
deck[-1]
#随即抽取一张牌
from random import choice
choice(deck)
choice(deck)
#查看一摞牌最上面三张和只看牌面是A打完牌的操作
deck[:3]
deck[12::13]#先抽出索引是12的那张牌,然后每隔13张牌拿一张
#仅仅实现__getitem__方法,这一摞牌就变成科迭代的了
for card in deck:
    print(card)
#反向迭代
for card in reversed(deck):
    print(card)
#使用in运算符,会按顺序做一次迭代搜索
Card('Q', 'hearts') in deck
Card('7', 'beasts') in deck
#对牌进行排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
##升序排序
for card in sorted(deck, key=spades_high):
    print(card)









