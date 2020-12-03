#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:57:40 2020

@author: samanthabuzzard
"""
import numpy as np

data=np.loadtxt('day2.txt',dtype='str')

count_valid=0

for i in range(len(data)):
    
    max=int(data[i,0].split('-')[1])
    min=int(data[i,0].split('-')[0])
    occurrences=data[i,2].count(data[i,1][0])
    if (occurrences<=max) and (occurrences>=min):
        count_valid=count_valid+1
        
print(count_valid)



count2_valid=0


for i in range(len(data)):
    
    place_1=int(data[i,0].split('-')[1])-1
    place_2=int(data[i,0].split('-')[0])-1
    letter=(data[i,1][0])
    if (data[i,2][place_1]==letter) or (data[i,2][place_2]==letter):
        count2_valid=count2_valid+1
    if (data[i,2][place_1]==letter) and (data[i,2][place_2]==letter): 
        count2_valid=count2_valid-1
        
print(count2_valid)