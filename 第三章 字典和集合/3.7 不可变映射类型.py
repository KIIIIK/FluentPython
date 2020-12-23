from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)
d_proxy
d_proxy[1]
d_proxy[2] = 'x'
d[2] = 'B'
d_proxy
d_proxy[2]



