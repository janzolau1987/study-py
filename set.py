#!/bin/usr/env python3
# -*- coding:utf-8 -*-

# 使用set
# set和dict类似，也是一组key集合，但不存储value。由于key不能重复，故在set中没有重复key
s = set([1, 1, 3, 2, 2, 3])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)

# 通过remote(key)可以删除元素
s.remove(4)
print(s)

# 做交集、并集操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

n1 = 255
n2 = 1000
print(hex(n2))
