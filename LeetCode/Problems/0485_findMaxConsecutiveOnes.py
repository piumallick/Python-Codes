#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:28:26 2020

@author: piumallick
"""
# Problem 485: Max Consecutive Ones
'''
Given a binary array, find the maximum number of 
consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the 
last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Note:

The input array will only contain 0 and 1.
The length of input array is a positive 
integer and will not exceed 10,000
'''

def findMaxConsecutiveOnes(nums):
    maximum = 0
    current = 0
    
    for x in nums:
        if (x == 1):
            current += 1
        else:
            if (current > maximum):
                maximum = current
            if (maximum >= len(nums)//2):
                return maximum
            current = 0
            
    return max(maximum, current)

# Testing
nums = [1,1,1,1,1,1,1,0]
print(findMaxConsecutiveOnes(nums))