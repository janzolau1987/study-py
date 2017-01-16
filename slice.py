#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 使用分片slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前三个元素方法
# 1.
print([L[0], L[1], L[2]])
# 2.
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# 3.
print(L[0:3])
print(L[:3])
print(L[-2:])
print(L[-2:-1])

# 样例：
# 创建一个0-99的数列
L = list(range(100))
print('数组内容:', L)
# 前10个数
print(L[:10])
# 后10个数
print(L[-10:])
# 前11-20个数
print(L[10:20])
# 前10个数，每两个取一个
print(L[:10:2])
# 所有数，每5个取一个
print(L[::5])
# 什么都不写，[:]可以原样复制一个list
print(L[:])

# tuple也是一种list,唯一区别是tuple不可变。
# tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串也可看成是一种list，每个元素就是一个元素
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
