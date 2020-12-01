#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:07:59 2020

@author: samanthabuzzard
"""

import numpy as np
data=np.loadtxt('day1.txt')

for i in range(len(data)):
    for j in range(len(data)):
        if data[i]+data[j]==2020:
            print(data[i], data[j])
            print(data[i]*data[j])


for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            if data[i]+data[j]+data[k]==2020:
                print(data[i], data[j], data[k])
                print(data[i]*data[j]*data[k])