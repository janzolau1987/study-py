#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用for/while循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

_sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    _sum += x
print(_sum)

print(range(5))
print(list(range(5)))

_sum = 0
for x in range(101):
    _sum += x
print(_sum)

_sum = 0
n = 99
while n > 0:
    _sum += n
    n -= 2
print(_sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,', x, '!')

n = 1
while n <= 100:
    if n > 10:  # 当n=11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n += 1
print('END')

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
