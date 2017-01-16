#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 使用map/reduce
# 1.map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# sorted排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score, reverse=True)
print(L3)
