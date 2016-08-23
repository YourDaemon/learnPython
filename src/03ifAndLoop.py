#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-8-22

@author: CPR119
'''

#if条件
x=1
if x:
    print 'True'
    
#for循环
names=['a','b','c']
for name in names:
    print name

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum+=x
print sum

sum=0
for x in range(101):
    sum+=x
print sum

sum=0
n=99
while n>0:
    sum+=n
    n-=2
print sum

sum=0
n=int(raw_input('input a number:'))
while n>0:
    sum+=n
    n-=2
print sum