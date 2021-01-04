fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=len)

def reverse(word):
    return word[::-1]
reverse('testing')
sorted(fruits, key=reverse)

#map,filter和reduce的现代替代品
list(map(fact, range(6)))
[fact(n) for n in range(6)]
list(map(factorial, filter(lambda n: n % 2, range(6))))
[factorial(n) for n in range(6) if n % 2]

#使用reduce和sum计算0~99之和
from functools import reduce
from operator import add
reduce(add, range(100))
sum(range(100))











