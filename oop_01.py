#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' 面向对象编程'

__author__ = 'JanzoLau'


class Student(object):
    __slots__ = ('__name', '__score')  # 用tuple定义允许绑定的属性名称

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    # getter/setter方法
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = score

    # 类似于java中toString
    def __str__(self):
        return 'Student Object (name:%s)' % self.__name

    # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
    # 也就是说，__repr__()是为调试服务的
    __repr__ = __str__


# 使用
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.b + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a
