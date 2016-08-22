#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-8-22

@author: CPR119
'''

#list 中文输出
L=['apple',123,True]
print u'输出：',L

#tuple
t=(1,2)
print(t)

t=()
print(t)

t=(1)
print t

t=(1,)
print t

t=(1,2,['a','b','c'])
print t

t[2][0]='A'
t[2][1]='B'
t[2][2]='C'
print t