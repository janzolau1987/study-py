#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 单字符串
print('Hello, world!')

# 会依次打印每个字符串，遇到逗号","会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')

# 打印整数
print(300)
print(100 + 200)
print("100 + 200 = ", 100 + 200)

# 输入输出
# name = input('please enter your name : ')
# print('Hello,', name)

# print absolute value of an integer
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# 字符串
print('I\'m ok')
print('I\'m learning\n Python')
print('\\\n\\')
# Python允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')
# '''...'''表示多行内容
print('''line1
...line2
...line3''')

# 布尔值
print(True)
print(False)
print(3 > 2)
print(True and False)
print(True or False)
print(not True)

# 字符串
print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
x = b'ABC'
print(x)
print("'ABC'.encode('ascii') =", 'ABC'.encode('ascii'))
print("'中文'.encode('utf-8') =", '中文'.encode('utf-8'))
print("b'ABC'.decode('ascii') =", b'ABC'.decode('ascii'))
print("b'\\xe4\\xb8\\xad\\xe6\\x96\\x87'.decode('utf-8') =", b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 字符串格式化
print('Hello, %s' % 'world.')
print('Hi, %s, you have $%d.' % ('Michael', 10000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
r = (85 - 72) / 72 * 100
print('%.1f' % r)
