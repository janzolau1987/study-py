#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用dic
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

# 判断key是否存在
print('Thomas' in d)

# 通过dic提供的get方法，如果key不存在，可以返回None,或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# 删除一个key
print(d.pop('Bob'))
print(d)
