l = [1, 2, 3]
id(l)
l *= 2
l
id(l)

t = (1, 2, 3)
id(t)
t *= 2
id(t)

t = (1, 2, [30, 40])
t[2] += [50, 60]
t
#查看字节码
import dis
dis.dis('s[a] += b')

#不要把可变对象放在元组里面
