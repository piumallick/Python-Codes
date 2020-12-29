#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:36:26 2020

@author: piumallick
"""

# Problem 169: Majority Element
'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(nums):
    
    count = 0
    candidate = 0

    for num in nums:
        
        if (count == 0):
            candidate = num
        if (num == candidate):
            count += 1
        else:
            count = 0
        #count += (1 if num == candidate else -1)
        print(count)
    return candidate
    
    # return max(nums,key=nums.count)    # run-time exceeded in leetcode
    
    
            
nums = [6,5,5]
print(majorityElement(nums))
# Output: 5

#############################################################################

# Alternate solution

def majorityElement(nums):
        nums.sort()
        return nums[len(nums) // 2]
    

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
# Output: 2    
    
