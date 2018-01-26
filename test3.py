# -*- coding: utf-8 -*-
# from datetime import datetime
#
# # # 获取当前datetime
# now = datetime.now()
# print(now)
# # 用指定日期时间创建datetime
# dt = datetime(2015, 4, 19, 12, 20)
# print(dt)
# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y', 'z'])
# p = Point(1, 2, 3)
# print(p.x)
# print(p.y)
# print(p.z)
# from collections import deque
#
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)
# from collections import defaultdict
#
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])
# from collections import OrderedDict
#
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)
# from collections import Counter
#
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)
import struct

# n = 10240099
# b1 = (n & 0xff000000) >> 24
# b2 = (n & 0xff0000) >> 16
# b3 = (n & 0xff00) >> 8
# b4 = n & 0xff
# bs = bytes([b1, b2, b3, b4])
# print(bs)
# print(struct.pack('>I', n))
# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use mds in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
