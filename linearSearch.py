#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:34:06 2019

@author: piumallick
"""

def linearSearch(array, x):
    
    for i in range(len(array)):
        if array[i] == x:
            return 'The element is present.'
        else:
            return 'The element is not present.'
        break
        
array = [5,6,4,2]
print(linearSearch(array, 4))

# Output:
 #The element is present.
 
#print(linearSearch(array, 9))
 # Output:
 # The element is not present.