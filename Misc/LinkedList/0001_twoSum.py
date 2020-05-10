#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:26:08 2020

@author: piumallick
"""
# Problem 1: TwoSum
'''
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def twoSum(nums, target):
    res = []
    for i in range(0, len(nums)-1):
        for j in range(1, len(nums)):
            if (nums[i] + nums[j] == target) and (i != j):
                res.append(i)
                res.append(j)
                return res
    

#Testing
nums = [1,5,5,2]
target = 10
print(twoSum(nums, target))
