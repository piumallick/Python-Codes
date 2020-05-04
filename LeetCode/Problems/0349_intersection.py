#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:17:20 2020

@author: piumallick
"""
# Problem 349: Intersection of Two Arrays
'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
'''

def intersection(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    intersection = nums1_set & nums2_set
    return (list(intersection))

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))