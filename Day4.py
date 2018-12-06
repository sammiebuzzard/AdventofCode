#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:13:35 2018

@author: samanthabuzzard
"""


import numpy as np
#import StringIO


input=np.genfromtxt('/Users/samanthabuzzard/Downloads/input4.txt',comments='%', dtype='str', delimiter=']')

input=input[input[:,0].argsort()]


shifts_list=[]

for entry in range(0, len(input)):
    if input[entry][1][1]=='G':
        shift_entries=1
        sameguard=1
        guard_id=((input[entry][1].split('#')[1]).split(' b')[0])
        guardasleep_minutes=np.zeros(60)
        sleep_total=0
        while (sameguard==1 and entry+shift_entries<len(input)):
            if input[entry+shift_entries][1][1]=='f':
                sleep_total=sleep_total+int(input[entry+shift_entries+1][0][15:17])-int(input[entry+shift_entries][0][15:17])
                for minutes_asleep in range (int(input[entry+shift_entries][0][15:17]),int(input[entry+shift_entries+1][0][15:17])):
                    guardasleep_minutes[minutes_asleep]=1    
                shift_entries=shift_entries+2
            else:
                sameguard=0
        shifts_list.append((guard_id, sleep_total, guardasleep_minutes))  
        

shifts_list=sorted(shifts_list, key=lambda tup: tup[0])

guards_list=[]
for entry in range(0,len(shifts_list)):
    if (entry==0 or shifts_list[entry][0]!=shifts_list[entry-1][0]):
        guard_id=shifts_list[entry][0]
        guard_total_asleep=shifts_list[entry][1]
        guard_total_minutes_asleep=shifts_list[entry][2]
        number_of_shifts=1
        while ((entry+number_of_shifts)<len(shifts_list) and shifts_list[entry][0]==shifts_list[entry+number_of_shifts][0]):
            guard_total_asleep=guard_total_asleep+shifts_list[entry+number_of_shifts][1]
            guard_total_minutes_asleep=guard_total_minutes_asleep+shifts_list[entry+number_of_shifts][2]
            number_of_shifts=number_of_shifts+1
        guards_list.append((guard_id, guard_total_asleep, guard_total_minutes_asleep))
        

guards_list=sorted(guards_list, key=lambda tup: tup[1])
max_asleep=int(guards_list[-1][0])
max_mins=np.argmax(guards_list[-1][2])
print(max_asleep*max_mins)


maximums=[]
for entry in range(0, len(guards_list)):
    maximums.append(max(guards_list[entry][2]))
print(int(guards_list[np.argmax(maximums)][0])*np.argmax(guards_list[np.argmax(maximums)][2]))