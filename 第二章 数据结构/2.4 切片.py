"""
2.4.2 对对象进行切片
"""
s = 'bicycle'
s[::3]
s[::-1]
s[::-2]

"""
2.4.4 给切片赋值
"""
l = list(range(10))
l[2:5] = 100#会报错,如果赋值的对象是一个切片,那么赋值语句的右侧必须是一个可迭代对象,即便只有一个值,也要把它转换成可迭代的序列
l[2:5] = [100]

"""
2.5 对序列使用+和*
"""
l = [1, 2, 3]
l * 5
5 * 'abcd'

board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
board

weird_board = [['_'] * 3] * 3
weird_board
weird_board[1][2] = 'O'
weird_board







