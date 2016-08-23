#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-8-22

@author: CPR119
'''

#dic 即map
d={'a':1,'b':2,'c':3}
print d['a']

d['a']=5
print d['a']

#print d['zhoulong']

if 'zhoulong' in d:
    print d['zhoulong']
else:
    print u'不存在'
    
print d.get('zhoulong',-1)
print d.get('zhoulong',None)
print d.get('zhoulong')

d.pop('c')
print d

#dict的key必须是不可变对象
t=(1,2,3)
d[t]=6
print d

#set
s=set([1,2,3])
print s

s.add(4)
print s

s.add(4)
print s

s.remove(4)
print s

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1=set([1,2,3])
s2=set([2,3,4])
print u'并集',s1&s2
print u'交集',s1|s2

#set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
#l=[1,2,3]
#s.add(l)

s.add(t)
print s