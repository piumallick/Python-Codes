#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:48:45 2020

@author: piumallick
"""
# Problem 53: Maximum Subarray
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which 
has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

def maxSubarray(a):
    max_so_far =a[0] 
    curr_max = a[0] 
   
    for i in range(1,len(a)): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max) 
    return max_so_far


# Testing:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarray(nums))
