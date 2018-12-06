#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:46:35 2018

@author: samanthabuzzard
"""

import numpy as np

input=np.loadtxt('/Users/samanthabuzzard/Downloads/input.txt')

a=0
for number in range(0,len(input)):
    a=a+input[number]
    
print(a)


b=0
count=0
match=0
loops=0
c=[]
while match==0:
    b=b+input[count]
    if b in c[:]:
        match=1
        print(b)
    count=count+1
    c.append(b)
    if count==len(input):
        count=0
        loops=loops+1
        print(loops)
    