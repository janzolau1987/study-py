#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# JSON使用
# 类型对应关系表
#   JSON类型           Python类型
#   {}                  dict
#   []                  list
#   "string"            str
#   1234.56             int/float
#   true/false          True/False
#   null                None

import json

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d = json.loads(json_str)
print(type(d))
print(d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score':std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(json_str, object_hook=dict2student))
