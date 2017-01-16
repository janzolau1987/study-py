#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 使用生成器Generator
# 在Python中，一边循环一边计算的机制，称为生成器：generator
L = [x * x for x in range(10)]  # list
g = (x * x for x in range(10))  # generator
print(L)
print(g)
print(next(g))
print(next(g))

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 如果一个函数定义中包含yield关键字，则此函数将是generator
        a, b = b, a + b
        n = n + 1
    # return 'done'


f = fib(6)
print(next(f))
print(next(f))
for n in f:
    print(n)


# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


o = odd()
print(next(o))
print(next(o))
print(next(o))

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(8)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return Value:', e.value)
        break

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator

