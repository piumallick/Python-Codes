#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:15:05 2020

@author: piumallick
"""

# Problem 540: Single Element in a Sorted Array

'''
You are given a sorted array consisting of only integers 
where every element appears exactly twice, except for one 
element which appears exactly once. Find this single element
 that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.
'''

def singleNonDuplicate(nums):
     
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 0:
        return 0
    
    start = 0
    end = len(nums) - 1
    
    while (start <= end):
        if (nums[start] != nums[start + 1]):
            return nums[start]
        if (nums[end] != nums[end - 1]):
            return nums[end]
        start += 2
        end -= 2
    return 0

# Testing
nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))
    