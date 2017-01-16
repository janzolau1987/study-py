#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 空函数
def nop():
    pass


# 从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新坐标
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


# 当不按顺序提供部分默认参数时，需要把参数名写上。enroll('Adam','M',city='beijing')
def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 如果是def add_end(L=[])就会出错，原因：
# Python函数在定义的时候，默认参数L的值就被计算出来，即[]，因为默认参数L也是一个变量
# 它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时L参数的内容就变了，不再是
# 函数定义时的[]
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n ** 2
    return sum


# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数
# 如果要限制关键字参数的名字，可以用命名关键字参数，如只接收city和job作为关键字参数
# def person(name, age, *, city, job):
#   print(name, age, city, job)

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
