#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# 使用内置模块datetime
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# datetime转换为timestamp
print(dt.timestamp())

# timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
