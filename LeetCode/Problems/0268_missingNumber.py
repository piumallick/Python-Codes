#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:12:02 2020

@author: piumallick
"""

# Problem 268: Missing Number

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''

def missingNumber(nums):
    length = len(nums)
    return length * (length + 1)//2 - sum(nums)
    
################################################
def missingNumber1(nums):
    s = sorted(nums)
    prev = -1
    
    for i in s:
        looking = prev + 1
        prev = i
        if i != looking:
            return looking
    
    return len(nums)

################################################
def missingNumber2(nums):
    a_Nums = set(nums)
    max_Num = len(a_Nums)
    all_Nums = set()
    
    for i in range(0, max_Num):
        all_Nums.add(i)
        
    setDiff = all_Nums.difference(a_Nums)
    
    if len(setDiff) == 1:
        return list(setDiff)[0]
    else:
        return max_Num

def missingNumber3(nums):
    a_Nums = set(nums)
    length = len(a_Nums)
    
    for i in range(0, length):
        if i not in a_Nums:
            return i
        
    return length


# Testing
nums = [4,0,2,1,3,5]
print(missingNumber(nums))