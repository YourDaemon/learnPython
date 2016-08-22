#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-8-22

@author: CPR119
'''

#一、调用函数
#help(abs)
print abs(-200)

#help(cmp)
print cmp(1,2)

print int('123')
print unicode(100)
print bool('')

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a=abs
print a(-1)

#二、定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print my_abs(-200)

#空函数 使用pass占位
def nop():
    age = 18
    if age >= 18:
        pass

#参数检查
def my_abs_checkin(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
print my_abs_checkin(-200)
#print my_abs_checkin('A')

#返回多个值
import math
def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny

x,y = move(100, 100, 1, math.pi / 4)
print x,y

r = move(100, 100, 1, math.pi / 4)
print r

#三、函数的参数
#默认参数
def power(x,n=2):
    s=1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5)
print power(5, 3)

#默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print add_end()
print add_end(['GAME'])


