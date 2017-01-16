#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Python yield使用浅析
print("原版：")
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

print(fab(5))

# 改进一:直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，
# 因为 fab 函数返回 None，其他函数无法获得该函数生成的数列
print("改版一：")
def fab2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

for n in fab2(5):
    print(n)

# 改进二：该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制
# 内存占用，最好不要用 List
# 通过iterable对象来迭代
print("改进二：")
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
for n in Fab(5):
    print n

# 改进三：想要保持第一版 fab 函数的简洁性，同时又要获得 iterable 的效果，yield 就派上用场
print("第三版:")
def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

for n in fab(5):
    print(n)

# 简单地讲，yield的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数，
# Python解释器会将其视为一个generator，调用fab(5)不会执行fab函数，而是返回一个iterable对象。
# 在for循环执行时，每次循环都会执行fab函数内部的代码，执行到yield b时，fab函数就返回一个迭代值，
# 下次迭代时，代码从yield b的下一条语句继续执行，而函数本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到yield。

# return的作用
# 在一个generator function中，如果没有return，则默认执行至函数完毕，如果在执行过程中return，则
# 直接抛出StopIteration终止迭代

# 例子
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

