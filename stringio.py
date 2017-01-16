#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO, BytesIO

# StringIO和ByteIO

# 写StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# 读StringIO
sf = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = sf.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())

fb = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(fb.read())
