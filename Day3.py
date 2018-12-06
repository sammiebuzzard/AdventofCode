#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:54:26 2018

@author: samanthabuzzard
"""


import numpy as np
#import StringIO


input=np.loadtxt('/Users/samanthabuzzard/Downloads/input3.txt',comments='%', dtype='str', delimiter=' ')
#0 is elf number
#1 is @
#2 is left comma down colon
#3 is width

steps_right = [int(i.split(',')[0]) for i in input[:,2]] 
steps_down = [i.split(',')[1] for i in input[:,2]]
steps_down = [int(i.split(':')[0]) for i in steps_down]

widths=[int(i.split('x')[0]) for i in input[:,3]] 
heights=[int(i.split('x')[1]) for i in input[:,3]] 



fabric_width=max([sum(x) for x in zip(steps_right,widths)])+1
fabric_height=max([sum(x) for x in zip(steps_down,heights)])+1

fabric=np.zeros((fabric_width,fabric_height))

for elf in range(0, len(steps_right)):
    for x_steps in range (steps_right[elf], steps_right[elf]+widths[elf]):
        for y_steps in range (steps_down[elf], steps_down[elf]+heights[elf]):
            fabric[x_steps, y_steps]=fabric[x_steps, y_steps]+1
            
print(len(np.where(fabric>1)[0]))


for elf in range(0, len(steps_right)):
    count=0
    for x_steps in range (steps_right[elf], steps_right[elf]+widths[elf]):
        for y_steps in range (steps_down[elf], steps_down[elf]+heights[elf]):
            if fabric[x_steps, y_steps]>1:
                count=count+1
                break
    if count==0:
        print(input[elf])
        break
    
    
    
