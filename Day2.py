#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:57:51 2018

@author: samanthabuzzard
"""


import numpy as np
import string

input=np.loadtxt('/Users/samanthabuzzard/Downloads/input2.txt',dtype='str')
twos=0
threes=0


for box in input:
    found_two=0
    found_three=0
    for letter in list(string.ascii_lowercase):
                occurrences=box.count(letter)
                if occurrences ==2:
                    found_two=1
                    twos=twos+1
                    break
    for letter in list(string.ascii_lowercase):
                occurrences=box.count(letter)
                if occurrences ==3:
                    found_threes=1
                    threes=threes+1
                    break
print(twos*threes)


for box1 in range(0, len(input)):
    for box2 in range(box1+1, len(input)):
        matches=sum(a==b for a, b in zip(input[box1], input[box2]))
        if matches>(len(input[box1])-2):
            break
    if matches>(len(input[box1])-2):
        break
answer=''
for letter in range (0, len(input[box1])):
    if input[box1][letter]==input[box2][letter]:
        answer=answer+(input[box1][letter])  
print(answer)