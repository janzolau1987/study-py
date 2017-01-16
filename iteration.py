#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Iterable

# 迭代iteration使用

# 1.dict迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, ':', v)

# 2.字符串迭代
for ch in 'ABC':
    print(ch)

# 判断一个对象是可迭代对象
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# python内置enumerate函数可将list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 同时引用两个变量
for x, y in [(1, 1), (2, 2), (3, 3)]:
    print(x, y)
