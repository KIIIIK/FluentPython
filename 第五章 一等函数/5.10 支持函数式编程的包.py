#operator模块
from functools import reduce
#使用reducr函数和一个匿名函数计算阶乘
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

#使用reduce和operator.mul函数计算阶乘
from functools import reduce
from operator import mul

def fact(n):
    return reduce(mul, range(1, n+1))


from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
upcase(s)
hiphenate = methodcaller('replace', ' ', '-')
hiphenate(s)
str.upper(s)

#使用functools.partial冻结参数
from operator import mul
from functools import partial
triple = partial(mul, 3)
triple(7)
list(map(triple, range(1, 10)))






