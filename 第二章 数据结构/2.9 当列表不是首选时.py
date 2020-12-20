"""
2.9.1 数组
"""
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
floats[-1]
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]
floats2 == floats

"""
2.9.2 内存试图
"""
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv)
memv[0]
memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4
numbers

"""
2.9.3 NumPy和SciPy
"""
import numpy
floats = numpy.loadtxt('floats-10M-lines.txt')
#精度和性能都较高的计时器
from time import perf_counter as pc

"""
2.9.4 双向队列和其他形式的队列
"""
from collections import deque
dq = deque(range(10), maxlen=10)
dq
dq.rotate(3)
dq
dq.rotate(-4)
dq
dq.appendleft(-1)
dq
dq.extend([11, 22, 33])
dq
dq.extendleft([10, 20, 30, 40])
dq
#其他队列库
##queue,multiprocessing,asyncio,heapq
#排序算法Timsort


