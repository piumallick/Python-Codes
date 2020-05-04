#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:00:43 2020

@author: piumallick
"""

# Problem 26: 26. Remove Duplicates from Sorted Array
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

"""

def removeDuplicates(nums):
    if (len(aNum) < 2):
        return len(nums)
    
    i = 0
    while (i < (len(nums)-1)):
        if (nums[i] == nums[i+1]):
            del nums[i]
        else:
            i += 1
    #print(nums)
    return (len(nums))
'''   
def removeDuplicates2(nums):
    if (len(aNum) < 2):
        return len(nums)
    
    count = 0
    uArr = []
    for (i in range(1, len(aNum))):
        if (aNum[i] )
 '''  
    
aNum = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(aNum))