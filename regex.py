#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

# 正则表达式
rm = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(rm)
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

# 切分字符串
print(re.split(r'\s+', 'a b    c'))
print(re.split(r'[\s\,\:]+', 'a,b:: c   d'))

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

# 贪婪匹配,加个?可以采用非贪婪匹配
m = re.match(r'^(\d+)(0*)$', '102300')
print(m.groups())

# 练习
re_mail1 = re.compile(r'^(\w+)@(\w+.\w+)$')
str1 = "someone@gmail.com"
print(re_mail1.match(str1).groups())
re_mail2 = re.compile(r"^<([\w\s]+)>\s+(\w+)@(\w+.\w+)$")
str2 = "<Tom Paris> tom@voyager.org"
print(re_mail2.match(str2).groups())

