#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文件读写

# 写文件
with open('./demo.txt', 'w', encoding='utf-8') as f:
    f.write('telephone=12321313')

# try:
#       f = open('./demo.txt', 'r', encoding='utf-8')
#       print(f.read())
# finally:
#       if f:
#          f.close()
with open('./demo.txt', 'r', encoding='utf-8') as f:
    # print(f.read())
    for line in f.readlines():
        print(line.strip())
