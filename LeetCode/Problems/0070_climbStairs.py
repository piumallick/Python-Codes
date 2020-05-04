#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:09:16 2020

@author: piumallick
"""
# Problem 6: Climbing Stairs
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

def climbStairs(n):
    if (n <= 2):
        return n
    
    a = 1
    b = 2
    result = 0
    for i in range(2, n):
        result = a + b
        a = b
        b = result
        
    return result

def climbStairs2(n):
    """
    :type n: int
    :rtype: int
    """
    c = [1, 1]
    for i in range(2, n+1):
        c.append(c[i-1] + c[i-2])
    return c[n]

# Testing
n = 0
print(climbStairs2(n))


