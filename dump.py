#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle

d = dict(name='Bob', age=20, score=80)

# 写序列化
with open('./dump.txt', 'wb') as f:
    f.write(pickle.dumps(d))

f = open('./dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 读序列化
with open('./dump.txt', 'rb') as f:
    # print(f.read())
    d1 = pickle.load(f)
    print(d1)
