#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:33:24 2020

@author: piumallick
"""
# Problem 645: Set Mismatch

'''
The set S originally contains numbers from 1 to n. 
But unfortunately, due to the data error, one of the numbers
 in the set got duplicated to another number in the set, 
 which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. 
Your task is to firstly find the number occurs twice and then find the number 
that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
'''

def findErrorNums(nums):
   
    nums = sorted(nums)
    
    presentSet = set(nums)
    actualSet = set([i for i in range(1, len(nums)+1)])
    
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            result = nums[i]
    
    diff = min(actualSet.difference(presentSet))
    return [result, diff]

nums = [1,2,2,4]
print(findErrorNums(nums))