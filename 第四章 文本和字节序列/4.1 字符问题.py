s = 'cafe'
len(s)
b = s.encode('utf8')
b
len(b)
b.decode('utf8')

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
octets










