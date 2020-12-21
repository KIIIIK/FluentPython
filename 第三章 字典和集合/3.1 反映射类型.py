from collections import abc

my_dict = {}
isinstance(my_dict, abc.Mapping)

tt = (1, 2, (30, 40))
hash(tt)
t1 = (1, 2, [30, 40])
hash(t1)
tf = (1, 2, frozenset([30, 40]))
hash(tf)

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e

"""
3.2 字典推导
"""
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]
country_code = {country: code for code, country in DIAL_CODES}
country_code
{code: country.upper() for country, code in country_code.items() if code < 66}


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
d['2']
d[4]
d[1]
d.get('2')
d.get(4)
d.get(1, 'N/A')
2 in d
1 in d




