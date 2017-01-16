#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from abstest import *
import math

print(my_abs(-2323))

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

print(add_end())
print(add_end())

# 关键字参数
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

# 递归函数
print(fact(1))
print(fact(5))
print(fact(100))
