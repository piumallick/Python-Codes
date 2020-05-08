#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:37:56 2020

@author: piumallick
"""
# Problem 1089: Duplicate Zeros
'''
Given a fixed length array arr of integers, 
duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, 
do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, 
the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, 
the input array is modified to: [1,2,3]

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
'''

def duplicateZeros(arr):
    i = 0
    while (i < len(arr)-1):
        if (arr[i] == 0):
            arr.insert(i+1, 0)
            print(arr)
            del arr[len(arr)-1]
            i = i + 2
        else:
            i = i + 1
       
        

# Testing
arr = [1,0,2,0,3]
print(duplicateZeros(arr))
    