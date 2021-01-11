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
















