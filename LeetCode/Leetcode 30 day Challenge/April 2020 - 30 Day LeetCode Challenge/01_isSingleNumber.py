#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:10:27 2020

@author: piumallick
"""
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
 
def isSingleNumber(nums):
        
        unique_numbers = set(nums)
        for element in unique_numbers:
            count = nums.count(element)
            if (count == 1):
                return element
            
print(isSingleNumber([2,2,3,4,3,4,1]))
    