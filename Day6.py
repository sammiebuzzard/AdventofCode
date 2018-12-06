#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:02:51 2018

@author: samanthabuzzard
"""

import numpy as np

input=np.genfromtxt('/Users/samanthabuzzard/Downloads/input6.txt',delimiter=',')
#input=np.array([[1,1],[1,6],[8,3],[3,4],[5,5],[8,9]])

x_points=input[:,0]
y_points=input[:,1]
max_grid=np.zeros((int(max(x_points)+3),int(max(y_points)+3)))
max_grid[:]=999

for x_value in range(0, int(max(x_points)+3)):
    for y_value in range(0, int(max(y_points)+3)):
        dist=(abs(x_value-x_points[:])+abs(y_value-y_points[:]))
        location=np.where(dist == dist.min())
        if len(location[0])==1:
            max_grid[x_value,y_value]=int(location[0])
max_grid=np.ma.masked_where(max_grid==999 , max_grid)
solution=0
while solution==0:   
    print(max_area)
    u, counts = np.unique(max_grid.flatten(), return_counts=True)
    max_area=u[np.argmax(counts[0:-1])]
    if (max_area in max_grid[0,:] or max_area in max_grid[-1,:] or max_area in max_grid[:,0] or max_area in max_grid[:,-1]):
        max_grid=np.ma.masked_where(max_grid==max_area , max_grid)
    else:
        solution=1
            
print(max(counts[0:-1]))


x_points=input[:,0]
y_points=input[:,1]
max_grid=np.zeros((int(max(x_points)+3),int(max(y_points)+3)))
max_grid[:]=999
area=0

for x_value in range(0, int(max(x_points)+3)):
    for y_value in range(0, int(max(y_points)+3)):
        dist=(abs(x_value-x_points[:])+abs(y_value-y_points[:]))
        total=sum(dist)
        if total<10000:
            area=area+1
            
print(area)


