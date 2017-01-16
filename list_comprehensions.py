#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

# 使用列表生成List Comprehensions

# 1.要生成list[1,2,3,4,5,6,7,8,9,10]可以用list(range(1,11))
print(list(range(1, 11)))

# 2.如果要生成[1*1,2*2,3*3,...,10*10]
L = []
for x in range(1, 11):
    L.append(x)
print(L)

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])

# 3.还可以使用两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 4.列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])

# 5.列表生成可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

# 6.把list中所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
