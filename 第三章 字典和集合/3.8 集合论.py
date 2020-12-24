l = ['spam', 'spam', 'eggs', 'spam']
set(l)
list(set(l))

#a | b返回合集,a & b返回交集,a - b返回差集

found = len(set(needles) & set(haystack))
found = len(set(needles).intersection(hystack))

"""
3.8.1 集合字面量
"""
s = {1}
type(s)
s
s.pop()
s
from dis import dis
dis('{1}')
dis('set([1])')

"""
3.8.2 集合推导
"""
from unicodedata import name
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}














