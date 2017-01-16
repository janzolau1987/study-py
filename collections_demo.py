#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import namedtuple, deque, defaultdict, OrderedDict

# 使用collections模块

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


# 基于OrderedDict实现一个FIFO的dict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containKey = 1 if key in self else 0
        if len(self) - containKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
