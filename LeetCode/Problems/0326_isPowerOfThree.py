#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:18:18 2020

@author: piumallick
"""
# Problem 326: Power of 3
"""
Power of 3:
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
"""

def isPowerOfThree(a):
    if (a == 0):
        return False
    while ((a % 3) == 0):
        a /= 3
        print('a:',a)
    return a == 1

a = 1
print(isPowerOfThree(a))