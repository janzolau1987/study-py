#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用list和tuple
classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
print('classmates[-2] =', classmates[-2])
print('classmates[-3] =', classmates[-3])
classmates.append('Adam')
print('classmates =', classmates)
classmates.insert(1, 'Jack')
print('classmates =', classmates)
print('classmates.pop() =', classmates.pop())
print('classmates =', classmates)
classmates[1] = 'Sarah'
print('classmates =', classmates)
L = ['Apple', 123, True]
print(L)
s = ['Python', 'Java', ['asp', 'php'], 'schema']
print(s)
print(len(s))
p = ['asp', 'php']
s = ['python', 'java', p, 'schema']
print(p[1])
print(s[2][1])
L = []
print(len(L))

# tuple和list非常类似，但tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
t = (1, 2)
print(t)
t = (1,)
print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 排序
a = ['c', 'b', 'a']
a.sort()
print(a)
