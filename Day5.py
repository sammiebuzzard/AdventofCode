#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:08:03 2018

@author: samanthabuzzard
"""

import numpy as np
import string

input=open('/Users/samanthabuzzard/Downloads/input5.txt','r')
long_string=input.readlines()[0]
long_string2=long_string

lower_case=string.ascii_lowercase
upper_case=string.ascii_uppercase
changes=1

while changes>0:
    old_string=long_string
    for letter in range(0,26):
        letter_pair=lower_case[letter]+upper_case[letter]
        long_string=long_string.replace(letter_pair, "")
        letter_pair=upper_case[letter]+lower_case[letter]
        long_string=long_string.replace(letter_pair, "")
    if old_string==long_string:
        changes=0
long_string=long_string.replace("\n", "")       
print('Final length is '+str(len(long_string)))
    

polymer_lengths=[]
for letter in range(0,26):
        long_string_test=long_string2.replace(upper_case[letter], "")
        long_string_test=long_string_test.replace(lower_case[letter], "")
        changes=1
        while changes>0:
            old_string=long_string_test
            for letter in range(0,26):
                    letter_pair=lower_case[letter]+upper_case[letter]
                    long_string_test=long_string_test.replace(letter_pair, "")
                    letter_pair=upper_case[letter]+lower_case[letter]
                    long_string_test=long_string_test.replace(letter_pair, "")
            if old_string==long_string_test:
                changes=0
                long_string_test=long_string_test.replace("\n", "")  
                polymer_lengths.append(len(long_string_test))

print('Min length is '+str(min(polymer_lengths)))
