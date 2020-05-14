#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:48:28 2020

@author: piumallick
"""
# Problem 172: Factorial Trailing Zeroes
'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
'''

def trailingZeroes(n):
    count_zeroes = 0
    x = 5
    while (n >= x):
        count_zeroes += n // x
        x = x * 5
    return count_zeroes
    


n = 30
print(trailingZeroes(n))