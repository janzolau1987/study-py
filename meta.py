#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'使用元类'


# type()
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# from hello import Hello
# h = Hello()
# h.hello()
# Hello, world.

